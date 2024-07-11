from typing_extensions import Self
import urllib
from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Query, Session
from sqlalchemy import text

class DatatableQueryExec():
    def __init__(self, request: Request, table_alias:str = "") -> None:
        self.request = request
        self.table_alias:str = ""
        self.draw:str = ""
        self.start: int= 0
        self.length:int = 0
        self.columns = []
        self.order = []
        self.search_value: str | None = None
        if table_alias:
            self.table_alias = table_alias        

    async def get_search_value(self)->str|None:
        return self.search_value

    async def execute_build_model(self, conn: Session, db_query: Query, row_builder:callable)->JSONResponse:
        prepare_query = await self.__prepare_query(db_query=db_query)
        
        result = []
        final_query = db_query
        search_sql = prepare_query["search_sql"]
        order_sql = prepare_query["order_sql"]

        if self.search_value:
            final_query = final_query.where(text(search_sql))
        if order_sql != "" and order_sql is not None:
            final_query = final_query.order_by(text(order_sql))
        q_rows = conn.execute(final_query).all()
        for row in q_rows:
            result.append(await row_builder(row))
        
        records_total = len(result)
        record_filtered = records_total

        return {
            'draw': self.draw if self.draw else 1,
            'recordsTotal': records_total,
            'recordsFiltered': record_filtered,
            'data': result
        }

    async def __prepare_query(self, db_query: Query)->str:
        # init all values
        await self.__init_request()
        search_sql = self.__apply_search(db_query)
        order_sql = self.__apply_order(db_query=db_query)
        return {'search_sql':search_sql, 'order_sql': order_sql}
    
    async def __init_request(self)->None:
        body = await self.request.body()
        byte_string = body
        decoded_string = byte_string.decode('utf-8')
        parsed_query = urllib.parse.parse_qs(decoded_string)
        if "search[value]" in parsed_query:
            self.search_value = parsed_query["search[value]"][0] 
        self.draw = int(parsed_query["draw"][0]) if "draw" in parsed_query else 1
        self.start = int(parsed_query["start"][0]) if "start" in parsed_query else 0
        self.length = int(parsed_query["length"][0]) if "length" in parsed_query else 10

        i = 0
        while f"columns[{i}][data]" in parsed_query:
            data = int(parsed_query[f"columns[{i}][data]"][0])
            name = parsed_query[f"columns[{i}][name]"][0] if f"columns[{i}][name]" in parsed_query else ",".join(parsed_query[f"columns[{i}][name][]"])
            searchable = parsed_query[f"columns[{i}][searchable]"][0].lower() == 'true'
            orderable = parsed_query[f"columns[{i}][orderable]"][0].lower() == 'true'
            col_data = {
                "data": data,
                "name": name,
                "searchable": searchable,
                "orderable": orderable,
            }
            self.columns.append(col_data)
            i += 1

        i = 0
        while f"order[{i}][column]" in parsed_query:
            order = {
                "column": int(parsed_query[f"order[{i}][column]"][0]),
                "dir": parsed_query[f"order[{i}][dir]"][0],
                "name": parsed_query[f"order[{i}][name]"][0] if f"order[{i}][name]" in parsed_query else ",".join(parsed_query[f"order[{i}][name][]"])
            }
            self.order.append(order)
            i += 1

    def __apply_search(self, db_query:Query)->str:  
        final_conditions = ""
        where_columns = []
        for col_data in self.columns:
            name = col_data["name"]
            searchable = col_data["searchable"]
            if searchable and self.search_value:
                if "," in name:
                    for col_name in name.split(','):
                        condition = f"{col_name} like '%{self.search_value}%'"
                        where_columns.append(condition)
                else:
                    condition = f"{name} like '%{self.search_value}%'"
                    where_columns.append(condition)

        if len(where_columns) > 0:
            or_where = " OR ".join(where_columns)
            final_conditions += f"({or_where})" 
        return final_conditions

    def __apply_order(self, db_query:Query)->str:
        final_order = ""
        _order = []
        for col_order in self.order:
            name = col_order["name"]
            dir = col_order["dir"]
            if "," in name:
                for _col_name in name.split(","):
                    order_sql = f"{_col_name} {dir}"
                    _order.append(order_sql)
            else:                
                order_sql = f"{name} {dir}"
                _order.append(order_sql)
        if len(_order) > 0:
            final_order = ", ".join(_order)
        return final_order
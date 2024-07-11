from setuptools import setup, find_packages

setup(
    name='eg-fastapi-datatable',
    version='1.0.1',
    packages=find_packages(),
    description='Fastapi Datatable',
    author='vicram10',
    author_email='victor.ramirez@egeek.com.py',
    #url='https://github.com/tu_usuario/mi_paquete',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'SQLAlchemy>=2.0',
    ],
)

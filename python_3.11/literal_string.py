from typing import LiteralString

def execute_query(conn, query: LiteralString, *params):
    ...

def your_code(conn, string_val:str):
    execute_query(conn, f"select * from table where id =?", string_val)
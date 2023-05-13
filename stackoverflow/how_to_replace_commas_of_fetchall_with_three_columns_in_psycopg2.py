import psycopg2
import pandas as pd

# con = psycopg2.connect(database="dbname",user="postgres",password="pwd",host="localhost",port= '5432')
# cursor_obj = con.cursor()
#
# sql = f"""SELECT COL1, COL2, COL3 FROM TABLE WHERE COL1= %S, COL3 = 1 ORDER BY COL1,COL2,COL3 ASC;"""
# row = cursor_obj.execute(sql,)
# resultset = cursor_obj.fetchall()

resultset = [('value1', 'value2', 1),
             ('value3', 'value4', 1),
             ('value5', 'value6', 1)]


list_data = [list(_val) for _val in resultset]

# converting all the values to string
fnl_data = [[str(_val) for _val in _data] for _data in list_data]

with open("yourtextfile.txt", "w") as f:
    for _val in list_data:
        # converting all list values to string
        # _val = [str(i) for i in _val]
        f.write("\t".join(_val) + "\n")


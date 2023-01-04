"""
pip install mysql-connector-python

"""

import json
from mysql import connector


class MySQLDBConn:
    def __init__(self, path):
        self.path = path
        self.cur = ''
        self.mysql_conn()

    def mysql_conn(self):
        conn = None
        try:
            with open(self.path) as f:
                conn_params = json.load(f)

            # connect to the MySQL server
            print('Connecting to the MySQL database...')
            db = connector.connect(**conn_params)
            db.autocommit = True

            # create a cursor
            self.cur = db.cursor()

            # execute a statement
            print('MySQL database version:')
            self.cur.execute('SELECT version()')

            # display the MySQL database server version
            db_version = self.cur.fetchone()
            print(db_version)

        except Exception as error:
            print(error)


if __name__ == '__main__':
    ms = MySQLDBConn('connection_details/conn_details.json')

import json
import sys
import psycopg2


class PostgesConn:
    def __init__(self, path):
        self.path = path
        self.postgres_conn()

    def postgres_conn(self):
        conn = None
        try:
            with open(self.path) as f:
                conn_params = json.load(f)

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**conn_params)
            conn.autocommit = True

            # create a cursor
            self.cur = conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            self.cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = self.cur.fetchone()
            print(db_version)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


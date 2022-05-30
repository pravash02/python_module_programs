from working_with_postgres.postgre_conn import PostgesConn
import json

class MainScript(PostgesConn):
    def __init__(self, path):
        print('Running Main Script')
        super().__init__(path)

    def run_query(self, sample_template):
        query = '''SELECT username, email, last_login FROM accounts'''
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            # print(rows)
            '''
                [
                 ('pravash02', 'prav@gmail.com', datetime.datetime(2022, 5, 3, 21, 42, 14, 340838)),
                 ('fini02', 'fini@gmail.com', datetime.datetime(2022, 5, 3, 21, 42, 36, 40501)),
                 ('sourabh02', 'sourabh@gmail.com', datetime.datetime(2022, 5, 3, 21, 42, 58, 589948))
                ]
            '''

            print(sample_template)
            for data in rows:
                sample_template['data']['Attributes']['UserName'] = data[0]
                sample_template['data']['Attributes']['EmailAddr'] = data[1]
                sample_template['data']['LastLogin'] = data[2]
                print(sample_template)

        except Exception as error:
            print(error)

        finally:
            # close the communication with the PostgreSQL
            self.cur.close()


if __name__ == '__main__':
    ms = MainScript('connection_details/conn_details.json')
    template_path = 'template/sample_json_frmt.json'
    with open(template_path) as f:
        sample_template = json.load(f)

    ms.run_query(sample_template)

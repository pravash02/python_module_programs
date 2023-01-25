import csv
import os
from marshmallow import Schema, fields, validate


# creating python class
class CreatingSchema(Schema):
    # first name as required input
    firstName = fields.Str(required=True, validate=validate.Length(min=1))
    lastName = fields.Str()
    email = fields.Email()


# read csv files
def read_csv_file(file_name):
    try:
        with open(f"{file_name}", 'r') as file:
          csvreader = csv.DictReader(file)
          for row in csvreader:
            # print(row)
            # deserializing in Python
            user_info = CreatingSchema().load(row)
            print(user_info)
        return csvreader
    except Exception as e:
        pass


def main(file_name=None):
    if file_name:
        dict_data = read_csv_file(file_name)
        print("Process completed")
    else:
        print("Invalid file path")


if __name__ == '__main__':
    file_path = os.getcwd()
    print('file_path - ', file_path)
    file_name = 'input_files/test.csv'
    main(file_name)

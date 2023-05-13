import json

input_dict = {}

input_length = int(input("Specify the range of input required"))


for i in range(input_length):
    key = input("")
    value = input("")
    input_dict[key] = value

formatted_dict = json.dumps(input_dict)   # to make the key and values double quote
print(formatted_dict)

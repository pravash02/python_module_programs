print("hello world")

int_a = 10
str_b = "string"
float_c = 2.45
list_d = [1, 2, 3]
dict_e = {1: 'a', 2: 'b'}
tup_f = (2, 3)
set_g = {()}
bool_f = True

print(int_a)

# datatype
print(type(int_a))
print(type(str_b))
print(type(float_c))
print(type(list_d))
print(type(dict_e))
print(type(tup_f))
print(type(set_g))
print(type(bool_f))


# f-string, format
print("This is a integer - ", int_a)

# question
query = "SELECT colncol_nameame FROM tatable_nameble"

col_name = "Name"
table_name = "Users"

# f-string
f_query = f"SELECT {col_name} FROM {table_name}"
print(f_query)

# .format
format_query = "SELECT {0} FROM {1}".format(col_name, table_name)
print(format_query)


list_d = ['USERS', 'DEPARTMENT', 'EMPLOYEE']
for table_name in list_d:
    f_query = f"SELECT NAME FROM {table_name}"
    print(f"tvalue query: {f_query}")

# length
print('length -', len(list_d))

# FOR LOOP WITH INDEX
for i in range(len(list_d)):        # i = 0 and 1 < 3
    print(i, list_d[i])
    print(list_d[i])        # access index values


# if elif else
if True:
    pass
else:
    pass

if condition:
    pass
elif condition2:
    pass
elif condition3:
    pass
else:
    pass

# while
while condtion:
    pass

# import
import json
import os


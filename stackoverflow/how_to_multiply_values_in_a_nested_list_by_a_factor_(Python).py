lst = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29]]

new_lst = [[2 * i for i in _lst] for _lst in lst]
print(new_lst)

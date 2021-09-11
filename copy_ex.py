import copy


# Shallow Copy---------------------------------------------------------#

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

new_list = copy.copy(old_list)
old_list[1][1] = 'AA'  # changes in old list affect new list

print("Old list:", old_list)  # o/p = ('Old list:', [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]])
print("New list:", new_list)  # o/p = ('New list:', [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]])


# Deep Copy---------------------------------------------------------#

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

new_list = copy.deepcopy(old_list)
old_list[1][0] = 'BB'  # changes in old list not affect new list
print("Old list:", old_list)  # o/p = ('Old list:', [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]])

print("New list:", new_list)  # o/p = ('New list:', [[1, 1, 1], [2, 2, 2], [3, 3, 3]])

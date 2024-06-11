List1 = [[1, 'a'], ['b'], [3], [4], [5]]
new_lst = sum(List1, [])
print(new_lst)

new_list = [val for sublist in List1 for val in sublist]
print(new_lst)


from itertools import chain
List1 = [[1, 'a'], [2], [3], [4], [5]]
flattened_lst = list(chain.from_iterable(List1))
print(flattened_lst)

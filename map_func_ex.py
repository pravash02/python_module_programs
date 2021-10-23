print("\n ---- map using lambda function ----")
celsius = [25, 32, 18, 13, 8]
print("inout - ", celsius)
fahrenheit = map(lambda x: x * 9 / 5 + 32, celsius)
print("results - ", list(fahrenheit))


print("\n ---- map using lambda function ----")
numbers = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14]]
print("inout - ", numbers)
length = map(len, numbers)
print("results - ", list(length))


print("\n ---- map using lambda function ----")
digits = (1, 2, 3, 4, 5)
print("input - ", digits)

def func1(val):
    return val + 5
results = map(func1, digits)
print("results - ", list(results))
# Q1. What is the output for below code ?
def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers()])
val = [lambda x: i * x for i in range(4)]

# output: "[6, 6, 6, 6]"

# Explanation -
"""
This is because the `multipliers()` function returns a list of four lambda functions, 
each of which takes a single argument x and multiplies it by the current value of `i`, which ranges from 0 to 3.
However, when the lambdas are actually called, the value of `i` will be whatever it was at the end of the loop that 
created them, which will be 3 in every case.
Therefore, each lambda will always multiply its argument by 3, resulting in the output of [6, 6, 6, 6] 
when [m(2) for m in multipliers()] is executed.
"""

# ---------------------------------------------------------------------- #

# Q2. What is the output for below code ?
x = 2
# while x < 15:
#     x =+ 1
print(x)

# output: "infinite loop"

# Explanation -
"""
Endless Loop as x value will be always 1 because of + operator is in after = operator, 
so there is no increment in x value, hence while loop will be true value end less.
"""

# ---------------------------------------------------------------------- #

# Q3. What is the output for below code ?
words = ["Artificial", "Intelligence"]
output = "".join([w[0].upper() for w in words])
print(output)

# output: "AI"

# Explanation -
"""
The program creates a string consisting of the first letter of each word in a list, capitalizes them, 
and joins them together into a single string.
"""

# ---------------------------------------------------------------------- #

# Q4. What is the output for below code ?
lst = [1, 2, 3, 4, 5]
print(lst[::-2][::-1][0])

# output: "1"

# Explanation -
"""
The slicing operator [::-2] returns a new list with every second element of the original list starting from the 
last element. So, it returns [5,3,1].
"""


# ---------------------------------------------------------------------- #

# Q5. What is the output for below code ?
def f(*args):
    return sum(args)


print(f(1, 2, 3, 4, 5))

# output: "15"

# Explanation -
"""
Basic concept to understand here is that one can pass multiple arguments to a function this way and they would be 
saved in args variable as tuple. sum() on a tuple would add the elements of the tuple.
"""

# ---------------------------------------------------------------------- #

# Q6. What is the output for below code ?
li = ['a']
li.extend("code")
print(li)

# output: "['a', 'c', 'o', 'd', 'e']"

# Explanation -
"""
The 'extend' command breaks the string (c,o,d,e) and add it as an individual element.
"""

# ---------------------------------------------------------------------- #

# Q7. What is the output for below code ?
arr = [4, 3, 2, 1, 0]
idx = arr[0]
arr[0], arr[idx] = arr[idx], arr[0]
print(arr)
# output: [0, 3, 2, 1, 4]

arr = [4, 3, 2, 1, 0]
arr[0], arr[arr[0]] = arr[arr[0]], arr[0]
print(arr)
# output: [4, 3, 2, 1, 0]

# Explanation -
"""

"""

# ---------------------------------------------------------------------- #

# Q8. write a code to get the desired output ?
lst = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29]]

output = [[0, 2, 4, 6, 8, 10], [12, 14, 16, 18, 20, 22], [36, 38, 40, 42, 44, 46], [48, 50, 52, 54, 56, 58]]

# Solution
new_lst = [[2 * i for i in _lst] for _lst in lst]
print(new_lst)

new_lst_2 = list(map(lambda inner_lst: list(map(lambda val: val * 2, inner_lst)), lst))
print(new_lst_2)


# ---------------------------------------------------------------------- #

# Q9. Whats the output ?
num = [3, 1, -6, 4, -1, 5]
print(num.reverse())

# output: None

# Explanation -
"""
list.reverse() is inplace function, so it returns None.
"""

# ---------------------------------------------------------------------- #

# Q 10. Write a logic to get the correct matching value
s = "SDBPDB SEC CODES EXCHANGE 20230512"
s1 = "SDBPDB SEC CODES"
s2 = "SDBPDB SEC CODES EXCHANGE"
s3 = "SDBPDB SEC"

lst = [s1, s2, s3]
matches = [item for item in lst if item in s]
print(matches)
longest_match = max(matches, key=len) if matches else None

if longest_match:
    print("Found:", longest_match)
else:
    print("No match found.")


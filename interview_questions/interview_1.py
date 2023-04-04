# Q1. What is the output for below code ?
k = "pythonic"
print(k[5:9])

# output: "nic"

# Explanation -
"""
Since `slicing` cannot be applied over non-existing elements, it will stop and return all the accessible ones.
"""

# ---------------------------------------------------------------------- #

# Q2. What is the output for below code ?
s = ['apple', 'applE', 'Apple']
s.sort(key=len)
print(s)

# output: "['apple', 'applE', 'Apple']"

# Explanation -
"""
The `sort()` method sorts a list in ascending order by default. 
The `case of the letters` is not taken into account when sorting by length.
"""

# ---------------------------------------------------------------------- #

# Q3. What is the output for below code ?
st = 'wxy'
print('z'.join(st))

# output: "wzxzy"

# Explanation -
"""
The `join()` method takes all items in an iterable and joins them into one string. 
A string must be specified as the separator.
"""

# ---------------------------------------------------------------------- #

# Q4. What is the output for below code ?
list1 = {22, 35, 51}
list1.add((5, 1))
list2 = {4, 51, 5, 1}
list2.intersection_update(list1)
print(list2)

# output: "{51}"

# Explanation -
"""
`add()` method, adds any element we give it to the desired set (unless it’s already present) and sets can 
store data of any type, there are no errors. 
`intersection_update()` method, modifies the set by removing all of the elements that the sets don’t have in common.
it is looking for elements that are present in both sets, regardless of their data type or how they are represented.
`{51}` is the only value that both sets have in common.
"""

# ---------------------------------------------------------------------- #

# Q5. What is the output for below code ?
x = [1, 2, 3, 4, 5]
for i in x:
    if i % 2 == 0:
        break
    print(i)

# output: "1"

# Explanation -
"""
Inside the `for` loop, there is an `if` statement that checks if the current element `i` is `even`. If `i` is even, 
the `break` statement is executed, which immediately terminates the `for` loop and control is transferred to the next 
statement after the loop.
"""

# ---------------------------------------------------------------------- #

# Q6. What is the output for below code ?
nums = [10, 20, 30]
temp = nums
nums.append(temp)
print(nums)

# output: "[10, 20, 30, [...]]"

# Explanation -
"""
In Python, when you assign a `list` to a new variable, you are not creating a new copy of the `list`. 
instead, both variables refer to the same `list` object in `memory`. Now when you append, this means that the 
`nums` list now contains itself as its last element.
The ellipsis ([...]) is used to represent a recursive reference to the list itself.
"""

# ---------------------------------------------------------------------- #

# Q7. What is the output for below code ?
list1 = [2, 4, 5, 'r', 7, 8, 12]
list2 = [3, 6, 9, 't', 2, 1, 6]
print(list1[2:-1] + list2[2:-1])

# output: "[5, 'r', 7, 8, 9, 't', 2, 1]"

# Explanation -
"""
Second argument in the `list` is exclusive so in the above example -1th element won't be included.
"""

# ---------------------------------------------------------------------- #

# Q8. What is the output for below code ?
stud = (1, 'Andy', 17, [90, 97, 96])
# stud[3] = [95, 97, 100]

# output: "TypeError: 'tuple' object does not support item assignment"

# Explanation -
"""
`tuples` in Python are immutable, which means their contents cannot be changed once they are created. 
`stud[3]` is a `list` and above statement is trying to replace that with a new list.
"""


# ---------------------------------------------------------------------- #

# Q9. What is the output for below code ?
def func(v1, v2, v3):
    print(v1 + v2 + v3)
# func('rge', v2='abc', 'prq')

# output: "SyntaxError: positional argument follows keyword argument"

# Explanation -
"""
You cant put a `positional` argument after `keyword` argument, Hence it will throw a syntax error.
"""

# ---------------------------------------------------------------------- #

# Q10. What is the output for below code ?
my_generator = (print(x, end=" ") or x for x in range(3))
for n in my_generator:
    print(n, end=" ")

# output: "0 0 1 1 2 2"

# Explanation -
"""
It looks like `generator comprehension`. 
Lets start with condition print(x, end=" ") or x,
if `print(x, end= ' ')` will be be false(and in that case will be always because return from that function is None) 
then x will be show. We looping for `range(3)` so we will have three numbers, `0,1,2`. So, 
for 0:
`print(0, end= ' ')` ==> it will print 0 with space but return will be None. So it will jump to -> `or x`
x ==> 0
so 1 line is 0 0,
moving forward same logic we will get 1 1 and 2 2.
"""

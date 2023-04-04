# Q1. What is the output for below code ?
D = dict()
for x in enumerate(range(2)):
    D[x[0]] = x[1]
    D[x[1]+7] = x[0]
print(D)

# output: "{0: 0, 7: 0, 1: 1, 8: 1}"

# Explanation -
"""
`enumerate(range(2))` function, which generates a sequence of `(index, value)` tuples for the range [0, 1].
"""

# ---------------------------------------------------------------------- #

# Q2. What is the output for below code ?
word = 'Python'
print(word[::-1][-1:-6:-2])

# output: "Pto"

# Explanation -
"""
`word[::-1]` creates a reversed copy of the string word, which is 'nohtyP'.
The expression `[-1:-6:-2]` creates a new list that starts at the last character of the reversed string, 
and ends before the sixth character from the end, moving in steps of -2 (i.e., backwards by 2 characters at a time).
"""

# ---------------------------------------------------------------------- #

# Q3. What is the output for below code ?
def fn(var1):
    var1.pop(1)

var1 = [1, 2, 3]
fn(var1)
print(var1)

# output: "[1, 3]"

# Explanation -
"""
Within the `fn` function, the pop method is called on var1 with argument 1. This removes the element at `index 1`.
"""

# ---------------------------------------------------------------------- #

# Q4. What is the output for below code ?
print("hello".replace("l", "L", 2))

# output: "heLLo"

# Explanation -
"""
The third argument in `replace` is the maximum number of replacements to perform. 
In this case, the value is `2`, which means that the method will replace the first two occurrences of `l` in the string.
"""

# ---------------------------------------------------------------------- #

# Q5. What is the output for below code ?
print("hello".join(["world", "python"]))

# output: "worldhellopython"

# Explanation -
"""
The `join` method concatenates the strings in the list using the string `hello` as a separator.
"""

# ---------------------------------------------------------------------- #

# Q6. What is the output for below code ?
greeting = "Hello World"
print(greeting.split()[::-1][0])

# output: "World"

# Explanation -
"""
The split method is called on the string with no arguments. This splits the string into a list of words, 
using whitespace as the delimiter.
"""

# ---------------------------------------------------------------------- #

# Q7. What is the output for below code ?
lst = [1, 2, 3, 4, 5]
print(lst[len(lst)//2:][::-1][0])

# output: "5"

# Explanation -
"""
`lst[len(lst)//2:]` ==> this will give [3, 4, 5] and then we reverse it so that becomes [5, 4, 3] and after that we are
accessing the `0th` element which is `5`.
"""

# ---------------------------------------------------------------------- #

# Q8. What is the output for below code ?
tpl = (10, 20, 30, 40)
print(tpl[::-1][list(enumerate(tpl, start=1))[-1][0]-1])

# output: "10"

# Explanation -
"""
The start=1 argument specifies that the index should start from 1 instead of the default 0. 
The resulting iterator looks like this: `[(1, 40), (2, 30), (3, 20), (4, 10)]`.
The `[-1]` index notation is used to retrieve the last element of the list, which is the tuple `(4, 10)`.
`[list(enumerate(tpl, start=1))[-1][0]-1]` ==> 3
and now, tpl[::-1][3] => 10
"""

# ---------------------------------------------------------------------- #

# Q9. What is the output for below code ?
itero = iter(list, 3)
print(next(itero))

# output: "[]"

# Explanation -
"""
`iter(list, 3)`, this creates an iterator that will keep producing items from the list until it reaches the value 3. 
Since 3 is not in the list, the iterator will simply produce all the items in the list and then stop.
In this case, the `list` is empty, so the iterator will stop immediately and the `next()` function will raise a 
`StopIteration` exception. This is why `([])` printed to the console.
"""

# ---------------------------------------------------------------------- #

# Q10. What is the output for below code ?
print(set(range(1, 3, -2)))

# output: "set()"

# Explanation -
"""
The answer will be an empty set because the range function with a step of -2 from 1 to 3 doesn't include any values 
in the range. Then it creates an empty constructor set().
"""

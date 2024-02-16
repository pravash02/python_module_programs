def add_subject1(name, subject, subjects=[]):
    subjects.append(subject)
    return {'name': name, 'subjects': subjects}


print(add_subject1.__defaults__)
print(add_subject1('person1', 'subject1'))
print(add_subject1('person2', 'subject1'))
print(add_subject1('person3', 'subject1'))
print(add_subject1.__defaults__)

    ## OR ##

def add_subject(name, subject, subjects=None):
    if subjects is None:
        subjects = []

    subjects.append(subject)
    return {'name': name, 'subjects': subjects}


print(add_subject.__defaults__)
print(add_subject('person1', 'subject1'))
print(add_subject('person2', 'subject1'))
print(add_subject('person3', 'subject1'))
print(add_subject.__defaults__)


def my_functions(a=1, b=2, c=3):
    pass


print(my_functions.__defaults__)

# --------------------------------------------- #

class Multiplier:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return (self.a * x**2) + (self.b * x**2) + (self.c * x**2)


func = Multiplier(2, 4, 6)
print(func(2))
print(func(4))
print(callable(func))

# --------------------------------------------- #

places = ["India", "London", "Poland", "Netherlands"]
for place in places:
    if place.startswith('Lo') or place.startswith('Po'):
        print(place)

        ## OR ##

    if place.startswith(('Lo', 'Po')):
        print(place)

# --------------------------------------------- #

set_ex = {1, 2, 3}
# dict_obj = {set_ex: "This is a Set"}
## Error - TypeError: unhashable type: 'set'

set_ex = frozenset({1, 2, 3})
dict_obj = {set_ex: "This is a Set"}

print(dict_obj[set_ex])

# --------------------------------------------- #

import pickle

a, b, c = 1, 2, 3

with open("data.pkl", "wb") as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

## READ ##
with open("data.pkl", "rb") as f:
    a = pickle.load(f)
    b = pickle.load(f)

print(f"{a = } {b = }")

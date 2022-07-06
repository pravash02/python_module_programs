import sys
from collections import deque
from collections.abc import Set, Mapping
from numbers import Number
from timeit import timeit
from pympler.asizeof import asizeof as getsize

# Note: getsize function was replaced for licence compatibility reasons
# so you may find slightly different results than seen in the video

import pytest


def normal_class_example():
    print('NORMAL CLASS EXAMPLE')

    class A:
        v = 42

        def __init__(self):
            self.x = 'hello'

    a = A()
    print('a dict:', a.__dict__)

    print('a.x (looked up in a dict):', a.x)
    a.x = 'world'
    print('a.x (looked up in a dict):', a.x)

    print('a.v (not found in a, looked up in A)', a.v)

    with pytest.raises(AttributeError):
        a.y  # we never defined y

    a.y = ':)'
    print('a.y', a.y)

    with pytest.raises(AttributeError):
        a.w  # we never defined w

    A.w = 'class variable'
    print('a.w (not found in a, looked up in A)', a.w)


def slots_class_example():
    print('SLOTS CLASS EXAMPLE')

    class A:
        __slots__ = ('x',)  # any iterable of strings is fine (except a string itself)
        v = 42

        def __init__(self):
            self.x = 'hello'

    a = A()

    with pytest.raises(AttributeError):
        print('a dict:', a.__dict__)  # nope! slotted classes don't have dicts by default

    print('a.x (looked up in slots):', a.x)
    a.x = 'world'  # can still modify slotted variables just fine
    print('a.x (looked up in slots):', a.x)

    print('a.v (not found in a, looked up in A)', a.v)

    with pytest.raises(AttributeError):
        a.y  # we never defined y

    with pytest.raises(AttributeError):
        a.y = ':('  # can't set a value for y, it's not one of the slots

    A.y = ':S'  # A is a type, which is not slotted, so we can still add y to A
    print('a.y (not found in a, looked up in A)', a.y)


def why_use_slots_example():
    print('WHY USE SLOTS EXAMPLE')

    class A:
        def __init__(self):
            self.x = 42

    class B:
        __slots__ = ('x',)

        def __init__(self):
            self.x = 42

    print('size of A instance:', sys.getsizeof(A()))  # has __dict__ and __weakref__
    print('size of B instance:', sys.getsizeof(B()))  # has __slots__ but no __dict__ or __weakref__

    print('recursive size of A instance:', getsize(A()))
    print('recursive size of B instance:', getsize(B()))
    print('size A / size B:', getsize(A()) / getsize(B()))


def why_really_use_slots_example():
    print('WHY REALLY USE SLOTS EXAMPLE')

    class A:
        def __init__(self):
            self.x = 42
            self.y = 42
            self.z = 42
            self.t = 42
            self.u = 42
            self.v = 42
            self.w = 42

    class B:
        __slots__ = 'x', 'y', 'z', 't', 'u', 'v', 'w'

        def __init__(self):
            self.x = 42
            self.y = 42
            self.z = 42
            self.t = 42
            self.u = 42
            self.v = 42
            self.w = 42

    print('size of A instance:', sys.getsizeof(A()))
    print('size of B instance:', sys.getsizeof(B()))

    print('recursive size of A instance:', getsize(A()))
    print('recursive size of B instance:', getsize(B()))
    print('size A / size B:', getsize(A()) / getsize(B()))


def slots_speed_considerations():
    print('SLOTS SPEED CONSIDERATIONS')

    class A:
        def __init__(self):
            self.x = 42

    class B:
        __slots__ = ('x',)

        def __init__(self):
            self.x = 42

    number = 10_000_000
    create_time = timeit(stmt="a=A()", globals=locals(), number=number)
    slotted_create_time = timeit(stmt="b=B()", globals=locals(), number=number)

    get_time = timeit(setup="a=A()", stmt="a.x", globals=locals(), number=number)
    slotted_get_time = timeit(setup="b=B()", stmt="b.x", globals=locals(), number=number)

    set_time = timeit(setup="a=A()", stmt="a.x = 0", globals=locals(), number=number)
    slotted_set_time = timeit(setup="b=B()", stmt="b.x", globals=locals(), number=number)

    # all close, not a reason to choose slots
    print(f'{create_time=}')
    print(f'{slotted_create_time=}')
    print(f'{get_time=}')
    print(f'{slotted_get_time=}')
    print(f'{set_time=}')
    print(f'{slotted_set_time=}')


def how_slots_work_example():
    print('HOW SLOTS WORK EXAMPLE')

    class A:
        pass

    class B:
        __slots__ = 'x', 'y', 'z'

    print('A dict:', A.__dict__)
    print('B dict:', B.__dict__)  # yes B has dict, B is a type, which is not slotted
    print('B.x:', B.x)  # it's a descriptor! explains why you can't use a default class variable

    b = B()
    b.x = "subscribe"  # calls B.__dict__['x'].__set__(b, "subscribe")
    print(b.x)  # calls B.__dict__['x'].__get__(b, B)


class Member:
    def __get__(self, instance, owner):
        if owner is None:
            return self

        val = ...  # C magic to access object at fixed offset within instance
        return val

    def __set__(self, instance, value):
        # C magic to set object at fixed offset within instance = value
        pass


def what_is_a_slot_example():
    print('WHAT IS A SLOT EXAMPLE')

    # assuming ssize_t = 8 bytes, ptr = 8 bytes

    class A:
        __slots__ = ()

    # A object --> +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ \
    # instance     |                    ob_refcnt                  | |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ | PyObject_HEAD
    #              |                    *ob_type                   | |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ /
    #              |                      ...                      |

    print("A basic size:", A.__basicsize__)  # size + ptr = 16 bytes

    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ \
    #              |                    *_gc_next                  | |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ | PyGC_Head
    #              |                    *_gc_prev                  | |
    # A object --> +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ /
    # instance     |                    ob_refcnt                  | \
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ | PyObject_HEAD
    #              |                    *ob_type                   | |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ /
    #              |                      ...                      |
    print("A instance size including gc:", sys.getsizeof(A()))  # size + 3 ptrs = 32 bytes

    class B:
        __slots__ = 'x', 'y', 'z'

    # B object --> +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ \               \
    # instance     |                    ob_refcnt                  | |               |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ | PyObject_HEAD |
    #              |                    *ob_type                   | |               |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ /               |
    #              |                       *x                      | \               | each is a slot
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ |               |
    #              |                       *y                      | | extra slots   |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ |               |
    #              |                       *z                      | |               |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ /               /

    print("B basic size:", B.__basicsize__)  # size + 4 ptrs = 40 bytes
    print("B instance size including gc:", sys.getsizeof(B()))  # size + 6 ptrs = 56 bytes

    class C:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.z = 0

    # C object --> +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    # instance     |                    ob_refcnt                  |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    #              |                    *ob_type                   |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    #              |                    *__dict__                  | -->  holds the x, y, z
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    #              |                    *__weakref__               |
    #              +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

    print("C basic size:", C.__basicsize__)  # size + 3 ptrs = 32 bytes
    print("C instance size including gc:", sys.getsizeof(C()))  # size + 5 ptrs = 48 bytes


def slots_with_inheritance():
    print('SLOTS WITH INHERITANCE')

    class A:
        __slots__ = 'x', 'y', 'z'

    class B(A):
        pass

    b = B()
    print("b dict:", b.__dict__)  # b will have a dict unless you also specify slots in B

    b.x = 10
    print("b dict:", b.__dict__)  # slotted variables stored in slot, not dict

    class C(A):
        __slots__ = ('t',)  # only specify additional slots

    c = C()
    print("c dict:", C.__dict__)
    c.x = 10
    c.t = 10
    # print(c.y)     # throws error
    print(c.x, c.t)

    a = A()
    print("a dict:", A.__dict__)
    a.x = 10
    a.y = 10
    a.z = 10
    print(a.x, a.y, a.z)




def slots_with_metaclass():
    print('SLOTS WITH METACLASS')

    with pytest.raises(TypeError):
        class Meta(type):
            __slots__ = 'a', 'b'  # metaclasses can only use empty slots

    class Meta(type):
        __slots__ = ()  # ok


def slots_with_dict():
    class A:
        __slots__ = ('__dict__',)  # dict but not weakref

    class B:
        __slots__ = ('__weakref__',)  # weakref but not dict

    class C:
        __slots__ = ()  # neither weakref nor dict

    class D:
        pass  # both weakref + dict

    class E:
        __slots__ = '__dict__', 'x', 'y'  # has dict, but x, y will not be in dict


def main():
    normal_class_example()
    # slots_class_example()
    # why_use_slots_example()
    # why_really_use_slots_example()
    # slots_speed_considerations()
    how_slots_work_example()
    # what_is_a_slot_example()
    # slots_with_inheritance()
    # slots_with_metaclass()
    # slots_with_dict()


if __name__ == '__main__':
    main()

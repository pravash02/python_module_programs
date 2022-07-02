def positional_only(a, b, c, /):
    print(f"{a=}, {b=}, {c=}")

def keywords_only(*, a, b, c):
    print(f"{a=}, {b=}, {c=}")

positional_only(1, 2, 3)
keywords_only(a=4, b=5, c=6)



def foo(a, b=3, *args, **kwargs):
    pass
foo('x')  # o/p: a=x, b=3, args=(), kwargs={}
foo('x', 'y')  # o/p: a=x, b=y, args=(), kwargs={}
foo('x', b='y')  # o/p: a=x, b=y, args=(), kwargs={}
foo('x', 'y', 'z', 'k')  # o/p: a=x, b=y, args=(z, k), kwargs={}
foo('x', c='y', d='y')  # o/p: a=x, b=3, args=(), kwargs={'c': 'y', 'd': 'k'}
foo('x', c='y', b='z', d='k')  # o/p: a=x, b=z, args=(), kwargs={'c': y, 'd': k}
foo('x', 'e', c='y', b='z', d='k')  # TypeError: foo() got multiple values for keyword argument 'b'



def alist(*args, **kwargs):
    print(args, kwargs)
alist(lst=[], tup=(), dic={})  # o/p = () {'tup': (), 'lst': [], 'dic': {}}
alist([1, 2], (3, 4), {5, 6})  # o/p = ([1, 2], (3, 4), set ([5, 6])) {}

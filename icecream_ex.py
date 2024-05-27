from icecream import ic

def foo(i):
    return i + 333

print(foo(123))     # 456
ic(foo(123))        # ic| foo(123): 456


a = 6
def half(i):
     return i / 2
b = half(ic(a))
ic(b)

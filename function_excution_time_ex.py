from timeit import timeit

trials = 10 ** 7
display_scale = 10 ** 9     # time in nanosceonds


def positional_only(a, b, c, /):
    # print(f"{a=}, {b=}, {c=}")
    pass


t1 = timeit(stmt="positional_only(1, 2, 3)", globals={'positional_only': positional_only}, number=trials)


def keywords_only(*, a, b, c):
    # print(f"{a=}, {b=}, {c=}")
    pass


t2 = timeit(stmt="keywords_only(a=1, b=2, c=3)", globals={'keywords_only': keywords_only}, number=trials)


print("normal func")
print(f'{t1=:.2f}\t\t func(1, 2, 3)')
print(f'{t2=:.2f}\t\t func(a=1, b=2, c=3)')

"""
@cache -  decorators for printing a function (fibonacci series,
    in this example) gets rid of the repetitive work.

This internally calls the lru_cache function(least-recently-used)
    On high level, This lru_cache functions stores the values in dictionary
    (cache = {}), and when we call anny function with the same argument
    it searches that key and returns the value.

"""

from functools import cache


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    print('\n ----printing fibonacci---- ')
    for i in range(5):
        print(i, fib(i))
    print('\n ----done---- ')


if __name__ == '__main__':
    main()

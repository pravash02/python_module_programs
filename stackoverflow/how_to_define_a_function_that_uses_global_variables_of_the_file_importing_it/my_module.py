import inspect

# def foo(gls=None):
#     if gls is None:
#         gls = globals()
#     # does something to gls
#     #     example: prints the size of all objects of the notebook/file being run


def foo():
    frame = inspect.currentframe().f_back
    gls = frame.f_globals
    print(gls['s'])

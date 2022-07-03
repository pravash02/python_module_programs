"""

f_back - go 1 function up in the stack
f_locals - look up the local variables

"""

import inspect


def print_callers_locals():
    frame = inspect.currentframe()
    print(frame)
    print(frame.f_back)
    caller_locals = frame.f_back.f_locals
    print(f"caller's locals: {caller_locals}")


def know_your_caller():
    x = 5
    s = "subscribe"
    print_callers_locals()


know_your_caller()

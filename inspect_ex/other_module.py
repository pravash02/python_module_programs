from inspect_ex.my_module import foo

s = "something to be accessed through globals()"
foo()           # foo does *not* have access to s
# foo(globals())  # foo has it
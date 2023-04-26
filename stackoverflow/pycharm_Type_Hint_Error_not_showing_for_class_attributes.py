class TestClass:
    a: int = "abc"

    def __init__(self):
        self.b: int = "abc"


t1 = TestClass()
t1.b = "def"

"""
The reason why PyCharm is only showing a type error at self.b: int = "abc" but not at a: int = "abc" or t1.b = "def" is 
because of the way type annotations and type checking work in Python.

Type annotations in Python are optional and provide hints to tools like PyCharm and mypy for type checking and analysis.
 However, Python itself does not enforce these annotations, and they do not affect the runtime behavior of the code.

When you define a: int = "abc", you are essentially providing a type hint that a is intended to be an integer. 
However, Python will still allow you to assign a string value to a, and will not raise any errors until you try to use 
a in a way that is not valid for a string (e.g., if you try to perform a mathematical operation on it).

Similarly, when you assign "def" to t1.b, Python will not raise any errors because it does not enforce the 
type annotation. However, PyCharm may still warn you that the assigned value is not consistent with the annotated type.

In contrast, when you define self.b: int = "abc" and try to create an instance of TestClass, 
PyCharm will raise a type error because self.b is annotated as an integer, 
but you are trying to assign a string value to it.


To enable PyCharm to show errors for type annotations and type checking, you can follow these steps:

Enable type checking: Go to Settings/Preferences > Editor > Inspections > Python > Type checker mode and 
select the appropriate mode (e.g. strict for full type checking or basic for minimal type checking).

Enable type hint validation: Go to Settings/Preferences > Editor > Inspections > Python > Type hints and enable the 
option Validate types of function parameters and return values.
"""
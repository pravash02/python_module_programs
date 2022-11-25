"""
A decorator is a design pattern in Python that allows a user to
    add new functionality to an existing object without modifying
    its structure.
Decorators are usually called before the definition of a function
    you want to decorate.

"""

import requests


def request_method(method):     # POST
    def decorator(function):    # create_
        def wrapper(*args, **kwargs):   # function's arguments
            return requests.request(method, *args, **kwargs)

        return wrapper
    return decorator


def request_method2(function):  # create_
    def wrapper(*args, **kwargs):  # function's arguments
        return requests.request('POST', *args, **kwargs)

    return wrapper


@request_method('POST')
def create_(self, url, headers, auth, json, timeout=5):
    pass

@request_method2
def create_(self, url, headers, auth, json, timeout=5):
    pass

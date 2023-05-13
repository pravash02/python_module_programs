async def func1():
    raise ValueError


async def func2():
    raise TypeError


async def main_func():
    results = await asyncio.gather(
        func1(),
        func2(),
        return Exception=True,
    )
    exceptions = [exc for exc in results if isinstance(exc, Exception)]
    if exceptions:
        raise ExceptionGroup("Couldn't execute", exceptions)

"""
ExceptionGroup: Couldn't execute (2 sub-exceptions)
+-+----------------------1------------------------------
| Traceback (most recent call last):
|   File "/hone/pravash/Projects/python311-release/exception-groups-py", line 5, in func1
|        raise ValueError
| ValueError
+------------------------2------------------------------
| Traceback (most recent call last):
|   File "/home/pravash/Projects/python311-release/exception-groups-py", line 9, in func2
|   raise TypeError
| TypeError: quota exceeded
"""
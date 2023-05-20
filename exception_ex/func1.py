from exception_ex.func2 import func2


def func1(d):
    try:
        func2(d)

    except Exception as e:
        raise Exception(str(e))

    finally:
        print("inside func1 method", d)

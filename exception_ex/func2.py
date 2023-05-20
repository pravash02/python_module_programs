def func2(d):
    try:
        a = 10
        b = 0
        print(a / b)

    except Exception as e:
        d['error'] = str(e)
        raise Exception(str(e))

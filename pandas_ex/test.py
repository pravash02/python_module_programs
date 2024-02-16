def test_func(v):
    found = True

    try:
        if v > 3:
            pass

        elif v / 0:
            found = True

    except Exception as e:
        found = False

    finally:
        return found


if __name__ == '__main__':
    lst = [0, 2, 3, 4, 0, 5, 1]
    fnd = []
    for val in lst:
        res = test_func(val)
        fnd.append(res)

    print(fnd)

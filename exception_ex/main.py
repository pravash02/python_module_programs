from exception_ex.func1 import func1

d = {}


def main():
    try:
        func1(d)

    except Exception as e:
        print("inside main method", d)


if __name__ == '__main__':
    main()

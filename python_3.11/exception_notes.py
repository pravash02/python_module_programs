def main() -> None:
    try:
        raise TypeError("The Type Error")
    except TypeError as error:
        error.add_note("Other Information")
        raise


if __name__ == '__main__':
    main()
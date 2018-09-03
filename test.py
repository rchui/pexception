import pexception


def main() -> None:
    another_really_long_name()


def another_really_long_name() -> None:
    another_really_really_really_long_name()


def another_really_really_really_long_name() -> None:
    another_really_really_really_really_long_name()


def another_really_really_really_really_long_name() -> None:
    raise Exception('Hello World')


if __name__ == '__main__':
    pexception.hook()
    main()

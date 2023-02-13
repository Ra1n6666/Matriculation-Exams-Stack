from stack import Stack


def main():
    stack = Stack()
    # []

    stack.push("example")
    # ['example']

    stack.top()
    # example

    stack.is_empty()
    # False

    stack.pop()
    # []

    stack.push("example")
    # ['example']

    stack.print_stack()
    # ['example']

    stack.is_empty()
    # True


if __name__ == "__main__":
    main()
    
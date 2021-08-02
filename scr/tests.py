import datetime


# up... -> B - Built-in

# value = 1  # G - Global

def outside_func():
    value = 3  # E - Enclosing

    def foo():
        # value = 2  # L - Local
        print(value)

    foo()


# foo()
# outside_func()


def get_current_date() -> str:
    return datetime.datetime.now().strftime("%d.%m.%Y")


def print_greeting():
    name = input("Name:")
    surname = input("Surname:")

    print("Hello, " + name + " " + surname + "! It's " + get_current_date())


# print_greeting()


# def recursive_func():
#     recursive_func()
#
#
# recursive_func()


def factorial(number: int) -> int:
    """
        return number * (number - 1) * (number - 2) *...* 1
        6! = 1*2*3*4*5*6 = 6*5*4*3*2*1
    factorial(6) = 6 * 5* 4*3*2*1
    """
    if number < 0:
        raise ValueError(f"Negative number: {number}")
    if number == 0:
        return 1
    return number * factorial(number - 1)


def test_factorial():
    """
        - number < 0
        - type of number
        + correct value (positive test)
        - too large number
        + number=0
    """

    value: int = 6
    expected_factorial: int = 720

    result = factorial(value)
    assert result == expected_factorial

    value = 0
    expected_factorial = 1
    result = factorial(value)
    assert result == expected_factorial

    value = -5
    try:
        factorial(value)
    except ValueError:
        pass
    else:
        assert False


if __name__ == '__main__':
    test_factorial()
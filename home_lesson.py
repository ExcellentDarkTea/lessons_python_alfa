# Создать декоратор congrats(), который выводит на экран сообщение "Well done, your result is <результат>",
# где "результат" - значение, возвращаемое из декорируемой функции.
from typing import Callable


def congrats(fn: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Well done, your result is" + fn(*args, **kwargs))
    return wrapper

@congrats
def function(temp1):
    print(temp1)
    return temp1

temp = " hello"
function(temp)

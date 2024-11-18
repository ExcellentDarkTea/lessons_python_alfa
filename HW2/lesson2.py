import logging
import datetime
from typing import Callable


# def check_authentication():
#     """
#     Check if user is authenticated in the system (identified)
#     """
#
#     if user_is_not_authenticated:
#         raise AUthenticationError()


def log_operation(fn: Callable) -> Callable:
    def wrapper():
        # do logging
        logging.error(f"Function {fn.__name__} is executed at {datetime.datetime.now()}")
        result = fn()
        # do logging
        logging.error(f"Function {fn.__name__} is finished at {datetime.datetime.now()}")
        logging.error(f"Result: {result}")
        return result
    return wrapper


@log_operation
def get_accounts() -> list:
    # check_authentication()
    """
    get accounts from Database
    prepare response from accounts
    return response to browser
    """
    logging.error("Running get_accounts")
    return ['26000001', '26000002']


# logging.error(get_accounts.__name__)
# data = get_accounts()
# logging.error(f"Final result: {data}")

#############################33


def log(fn: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        started_at = datetime.datetime.now()
        logging.error(f"Function {fn.__name__} started at {started_at}.")
        result = fn(*args, **kwargs)  # Execute the decorated function
        finished_at = datetime.datetime.now()
        logging.error(f"Function {fn.__name__} finished at {finished_at}.")
        return result
    return wrapper



def log_with_exc(fn: Callable) -> Callable:
    def wrapper():
        started_at = datetime.datetime.now()
        logging.error(f"Function {fn.__name__} started at {started_at}.")
        try:
            result = fn()  # Execute the decorated function
        except Exception as e:
            logging.critical(f"Caught error: {e}")
            raise
        else:
            finished_at = datetime.datetime.now()
            logging.error(f"Function {fn.__name__} finished at {finished_at}.")
            return result
    return wrapper


@log_with_exc
def show_greeting():
    print("Hello!")
    raise ValueError("Ha-ha!")


# show_greeting()

@log
def factorial(number) -> int:
    if number < 0:
        raise ValueError(f"Negative number: {number}")
    if number == 0:
        return 1
    return number * factorial(number - 1)


factorial(5)


def power(x):
    def internal(y):
        return y**x
    return internal


#p = power(4)  # def internal(y): return y**4
#print(p)
#print(p(2))  # 2**4 == 16


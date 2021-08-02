#функцию is_primary(), которая принимает целое число и возвращает, является ли число простым ( булевый результат ).
#функцию test_primary(), которая реализует тестирование функции is_primary() с использованием assert. Предусмотреть как позитивные тесты (то, что ожидается от функции), так и негативные (реакция на внештатные ситуации).
import math

def is_primaty(numb:int) -> bool:
     if type(numb) == int:
       if numb < 2:
          key = 0
          return False

       key = 1
       lim = int(math.sqrt(numb)+1)
       for i in range(2, lim):
           if numb % i == 0:
               key = 0
               break

       if key == 0:
           return False
       else:
           return True
     else:
         raise ValueError(f'Error type {numb}')

def test_primary():
    """
    - error type: string, float
    - number<2
    + correct value return true
    + correct value return false
    """
    value = 125
    answer = False
    result = is_primaty(value)
    assert result == answer

    value = 149
    answer = True
    result = is_primaty(value)
    assert result == answer

    value = -20
    answer = False
    result = is_primaty(value)
    assert result == answer

    value = 20.5
    try:
        is_primaty(value)
    except ValueError:
        pass
    else:
        assert False

    value = 'str'
    try:
        is_primaty(value)
    except ValueError:
        pass
    else:
        assert False

if __name__  == '__main__':
#    n = int(input("n="))
#    print (is_primaty(n))
    test_primary()

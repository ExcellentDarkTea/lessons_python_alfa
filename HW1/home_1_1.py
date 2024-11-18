#Create a function is_primary(), which takes an integer and returns whether the number is prime ( boolean result ).
#Create a function test_primary(), which implements testing of the is_primary() function using assert. Provide both positive tests (what is expected from the function) and negative tests (reaction to out-of-order situations).
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

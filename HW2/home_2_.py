
import re
from typing import Callable


#1. Create a report() function that takes the text of an error message and prints it to the screen.
def report(error):
    print(error)

#Create the catch() decorator, which allows you to catch file handling exception errors that occur in the function being decorated.
def catch(fn: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            result = {}
            result = fn(*args, **kwargs)
            return result
        except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
            report(e)

    return wrapper

#2. Write a function get_word_stats(). which takes the path to a text file,
# reads it and returns a dictionary in which
# keys are the words in the file,
# values are the number of times they are repeated in the file.
@catch
def get_word_stats(filename: str):
    glosary = {}
    frequency = {}

    with open(filename, 'r') as f:
        document_text = f.read()
        text_string = document_text.lower()

    match_pattern = re.findall(r'[a-z]{1,30}', text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    for words in frequency.keys():
        glosary[words] = frequency[words]
    #print(glosary)

    return glosary


#------------------------------------------------
#3. get_word_stats_second - copypaste function, but with a new decorator via zamikanie
#------------------------------------------------
# Implement the make_catch() closure, which accepts the fn function parameter.
#Copy the catch() decorator inside the closure, which should use the fn function instead of the report function.

def make_catch(fn: Callable) -> Callable:
    def catch_1(decor_fn: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                result = {}
                result = decor_fn(*args, **kwargs)
                return result
            except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
                fn(*args, **kwargs)
        return wrapper
    return catch_1

my_decorstor = make_catch(report)

@make_catch(report)
def get_word_stats_second(filename):
    glosary = {}
    frequency = {}

    with open(filename, 'r') as f:
        document_text = f.read()
        text_string = document_text.lower()

    match_pattern = re.findall(r'[a-z]{1,30}', text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    for words in frequency.keys():
        glosary[words] = frequency[words]
    #print(glosary)
    return glosary

#------------------------------------------------
#check the operation of the function, decorator and closure if they work and start at all
#------------------------------------------------

name = 'home2.txt'  #real path guidance file by name
#name = 'C:/Users/Robotics/PycharmProjects/course/scr/home2.txt' # alternative a real path guidance file
#name = "text.txt"  #non-existent file
text = get_word_stats(name)
text2 = get_word_stats_second(name)
print(text)
print(text2)

#------------------------------------------------
#the positivity test
#------------------------------------------------

def test_positive():
    value = 'home2.txt'
    answer = {'we': 2, 'all': 2, 'live': 2, 'in': 1, 'a': 1, 'yellow': 4, 'submarine': 4}
    result = get_word_stats(value)
    assert result == answer

    value = 'home2.txt'
    answer = {'we': 2, 'all': 2, 'live': 2, 'in': 1, 'a': 1, 'yellow': 4, 'submarine': 4}
    result = get_word_stats_second(value)
    assert result == answer

test_positive()
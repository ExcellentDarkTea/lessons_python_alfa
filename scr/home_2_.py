
import re
from typing import Callable


#Создать функцию report(), которая принимает текст сообщения об ошибке и печатает его на экран.
def report(error):
    print(error)

#Реализовать декоратор catch(), который позволяет перехватить ошибки исключений работы с файлом,
# возникающих в декорируемой функции.
def catch(fn: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            result = {}
            result = fn(*args, **kwargs)
            return result
        except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
            report(e)

    return wrapper


#1. Написать функцию get_word_stats(). которая принимает путь к текстовому файлу,
# вычитывает его и возвращает словарь, в котором
# ключи - это слова в данном файле,
# значения - количество их повторений в файле.
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
# Задание 3. get_word_stats_second - копипаст функция, но с новим декоратором через замикание
#------------------------------------------------

#Реализовать замыкание make_catch(), которое принимает параметр fn - функцию.
# Внутрь замыкания скопировать декоратор catch(), который вместо функции report должен использовать функцию fn.

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
#проверка работы функции, декоратора и замыкания сто они вообще работают и запускаються
#------------------------------------------------

name = 'home2.txt'  #реальнй файл указаний по имени
#name = 'C:/Users/Robotics/PycharmProjects/course/scr/home2.txt' # аналогично реальний файл указаний по пути
#name = "text.txt"  #несуществующий файл
text = get_word_stats(name)
text2 = get_word_stats_second(name)
print(text)
print(text2)

#------------------------------------------------
#релаизация позитинвного теста
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
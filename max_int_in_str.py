import re


"""
Есть строка из произвольных символов, нужно найти в ней максимальный int.
"""

s = "df122gk123dfgd124dfghjk1sdfg2db99"

def test_re():
    numbers = list(map(int, re.findall(r'\d+', s)))  # \d+ — последовательность из 1 или более цифр
    # numbers = [int(_) for _ in re.findall(r'\d+', s)]
    print(numbers)
    print(max(numbers))

def test_isdigit():
    numbers = list(map(int, ''.join(_ if _.isdigit() else ' ' for _ in s).split()))
    print(numbers)
    print(max(numbers))

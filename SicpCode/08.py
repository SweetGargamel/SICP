# Lists

from tkinter import N

#from 09 import numer


odds = [41, 43, 47, 49]
len(odds)
odds[1]
odds[0] - odds[3] + len(odds)
odds[odds[3]-odds[2]]
odds[4]
odds[-1]


# Containers

digits = [1, 8, 2, 8]
1 in digits
'1' in digits
[1, 8] in digits
[1, 2] in [[1, 2], 3]

digits[:]
digits[1:]
digits[3:1:-1]
digits[::-1]

# For statements

def count_while(s, value):
    """Count the number of occurrences of value in sequence s.

    >>> count_while(digits, 8)
    2
    """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

def count_for(s, value):
    """Count the number of occurrences of value in sequence s.

    >>> count_for(digits, 8)
    2
    """
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total






pairs = [[1, 2], [2, 3], [2, 3, 4]]
for x in pairs:
    if len(x) == 2:
        x1, x2 = x
        print(x1)
        print(x2)
    # print(y)


# Ranges

list(range(5, 8))
list(range(4))
len(range(4))

# range(n): iterable
def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for i in range(3):
        if i == 1:
            continue
        print('Go Bears!')


# List comprehensions

odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x for x in odds if 25 % x == 0]

def divisors(n):
    """Return the integers that evenly divide n.

    >>> divisors(1)
    [1]
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    >>> [n for n in range(1, 1000) if sum(divisors(n)) == n]
    [1, 6, 28, 496]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]


def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    numerals.values()
    numerals.keys()
    numerals.items()
    list(numerals.values())
    sum(numerals.values())
    dict([(3, 9), (4, 16), (5, 25)])
    numerals.get('X', 0)
    numerals.get('X-ray', 0)
    {x: x*x for x in range(3,6)}

    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}


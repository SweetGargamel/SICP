
""" Homework 3: Recursion """

HW_SOURCE_FILE = 'hw03.py'


#####################
# Required Problems #
#####################


def integrate(f, l, r, min_interval):
    """Return the definite integration of function f over interval 
    [l,r], with interval length limit min_interval.

    >>> abs(integrate(lambda x: x * x, 1, 2, 0.01) - (7 / 3)) < 0.001
    True
    >>> abs(integrate(lambda x: x, 1, 2, 0.01) - 1.5) < 0.0001
    True
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'integrate', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    sum=0
    if ((r-l) >= min_interval):
        sum=integrate(f, l, (r+l)/2, min_interval)+integrate(f, (r+l)/2, r, min_interval)
    else:
        sum=(f(l)+f(r))*(r-l)/2
    return sum



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    5
    >>> pingpong(8)
    4
    >>> pingpong(15)
    3
    >>> pingpong(21)
    5
    >>> pingpong(22)
    6
    >>> pingpong(30)
    10
    >>> pingpong(68)
    0
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    -1
    >>> pingpong(72)
    -2
    >>> pingpong(100)
    6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def haveSix(n):
        if n%10==6:
            return True
        elif n==0:
            return False
        else:
            return haveSix(n//10)
    def number_of_six(n):
        if n % 6 == 0:
            return True
        else:
            return haveSix(n)

    def helper(i,direction):
        if i==n:
            return direction
        if number_of_six(i):
            return helper(i+1,direction*(-1))+direction
        else:
            return helper(i+1,direction)+direction
    return helper(1,1)




def balanced(s):
    """Returns whether the given parentheses sequence s is balanced.
    >>> balanced('()')
    True
    >>> balanced(')')
    False
    >>> balanced('(())')
    True
    >>> balanced('()()')
    True
    >>> balanced('()())')
    False
    >>> balanced('()(()')
    False
    """
    if len(s) == 0:
        return True
    if len(s)%2!=0:
        return False
    else:
        while(len(s)!=0):
            indexL=s.find('(')
            indexR=s.find(')')
            if indexL>=indexR:
                return False
            elif(indexL<0 or indexR<0):
                return False
            if indexR<len(s):
                s=s[:indexL]+s[indexL+1:indexR]+s[indexR+1:]
            else:
                s=s[:indexL]+s[indexL+1:]
        return True
    def divide(s, k):
        """Divide the given parentheses sequence s into two parts at position k.
        >>> left, right = divide('()()', 2)
        >>> left
        '()'
        >>> right
        '()'
        >>> left, right = divide('(())()', 4)
        >>> left
        '(())'
        >>> right
        '()'
        >>> left, right = divide('(())()', 6)
        >>> left
        '(())()'
        >>> right
        ''
        """
        return (s[:k], s[k:])

    def peel(s):
        """Peel off the leftmost and rightmost parentheses in s to obtain the
        internal part of the parentheses sequence.
        >>> peel('(())')
        '()'
        >>> peel('()')
        ''
        >>> peel('))((')
        ')('
        """
        return s[1:-1]

    def match(s):
        """Returns whether the leftmost and the rightmost parentheses in s match.
        >>> match('()')
        True
        >>> match('()()')
        True
        >>> match('()))')
        True
        >>> match('))')
        False
        >>> match(')())')
        False
        """
        return s[0] == '(' and s[-1] == ')'

    "*** YOUR CODE HERE ***"



def count_change(total, money):
    """Return the number of ways to make change for total,
    under the currency system described by money.

    >>> def chinese_yuan(ith):
    ...     if ith == 1:
    ...         return 1
    ...     if ith == 2:
    ...         return 5
    ...     if ith == 3:
    ...         return 10
    ...     if ith == 4:
    ...         return 20
    ...     if ith == 5:
    ...         return 50
    ...     if ith == 6:
    ...         return 100
    >>> def us_cent(ith):
    ...     if ith == 1:
    ...         return 1
    ...     if ith == 2:
    ...         return 5
    ...     if ith == 3:
    ...         return 10
    ...     if ith == 4:
    ...         return 25
    >>> count_change(15, chinese_yuan)
    6
    >>> count_change(2, chinese_yuan)
    1
    >>> count_change(49, chinese_yuan)
    44
    >>> count_change(49, us_cent)
    39
    >>> count_change(49, lambda x: 2 ** (x - 1))
    692
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def returnMaxIndex(total,index,money):
        #返回moeny中的最大面值的index
        if not money(index+1):
            return index
        elif money(index+1)>total:
            return index
        else:
            return returnMaxIndex(total,index+1,money)

      
    def helper(currentMoney,maxIndex,money):#传入我们使用的最大面额
        if money(maxIndex):
            leftMoney=currentMoney - money(maxIndex)
            
            if maxIndex==1:#如果我们已经来到了最小面额
                if leftMoney==0:#如果面额已经兑换完
                    return 1
                elif leftMoney>0:
                    return helper(leftMoney,maxIndex,money)     #+helper(currentMoney,maxIndex-1,money)
                else:
                    return 0
            else:
                if leftMoney==0:
                    return 1 +helper(currentMoney,maxIndex-1,money)
                elif leftMoney>0:
                    return helper(leftMoney,maxIndex,money)+helper(currentMoney,maxIndex-1,money)
                else:
                    return helper(currentMoney,maxIndex-1,money)
        else:
            return 0
    maxIndex=returnMaxIndex(total,1,money)
    return helper(total,maxIndex,money)    
    
    


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    another=6-start-end
    if (n==1):
        print_move(start,end)
    else:
        move_stack(n-1, start, another)
        print_move(start,end)
        move_stack(n-1, another, end)


def multiadder(n):
    """Return a function that takes N arguments, one at a time, and adds them.
    >>> f = multiadder(3)
    >>> f(5)(6)(7) # 5 + 6 + 7
    18
    >>> multiadder(1)(5)
    5
    >>> multiadder(2)(5)(6) # 5 + 6
    11
    >>> multiadder(4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
    26
    >>> from construct_check import check
    >>> # Make sure multiadder is a pure function.
    >>> check(HW_SOURCE_FILE, 'multiadder',
    ...       ['Nonlocal', 'Global'])
    True
    """
    "*** YOUR CODE HERE ***"

    def helper(n,currentSum):
        def inner(x):
            if n==1:
                return currentSum+x
            return helper(n-1,currentSum+x)
        return inner
    return helper(n,0)

    # if n==0:
    #     return None
    # if n==1:
    #     return lambda x: x
    # def helper(x):
    #     if len(listn) == n-1:
    #         sum=x
    #         for i in listn:
    #             sum=i+sum
    #         return sum
    #     else:
    #         listn.append(x)
    #         return helper
    # return helper
    # dic=[0,1]
        
    # def helper(x):
    #     if listn[1]==n:
    #         return listn[0]+x
    #     else:
    #         listn[0]=listn[0]+x
    #         listn[1]=listn[1]+1
    #         return helper
    # return helper

##########################
# Just for fun Questions #
##########################


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
  

    
    return (lambda f: f(f))(lambda f: lambda n: 1 if n == 0 else mul(n, f(f)(sub(n, 1))))
    #下面是gpt代码
    #return (lambda f: (lambda x: f(f, x)))(lambda self, n: 1 if n == 0 else mul(n, self(self, sub(n, 1))))

'''
Given mystery function Y, complete fib_maker and number_of_six_maker so that the given doctests work correctly.

When Y is called on fib_maker, it should return a function which takes a positive integer n and returns the nth Fibonacci number.

Similarly, when Y is called on number_of_six_maker it should return a function that takes a positive integer x and returns the number of times the digit 6 appears in x.


'''
def Y(f): return (lambda x: x(x))(lambda x: f(lambda z: x(x)(z)))
def fib_maker(f): return  lambda n: n if n < 2 else f(n-1) + f(n-2)

    
def number_of_six_maker(f):  return lambda n:0 if (n//10 == 0 and  n!=6 )else f(n//10) +(1 if n%10 == 6 else 0)


my_fib = Y(fib_maker)
my_number_of_six = Y(number_of_six_maker)

# This code sets up doctests for my_fib and my_number_of_six.

my_fib.__name__ = 'my_fib'
my_fib.__doc__ = """Given n, returns the nth Fibonacci nuimber.

>>> my_fib(0)
0
>>> my_fib(1)
1
>>> my_fib(2)
1
>>> my_fib(3)
2
>>> my_fib(4)
3
>>> my_fib(5)
5
"""

my_number_of_six.__name__ = 'my_number_of_six'
my_number_of_six.__doc__ = """Return the number of 6 in each digit of a positive integer n.

>>> my_number_of_six(666)
3
>>> my_number_of_six(123456)
1
"""

    

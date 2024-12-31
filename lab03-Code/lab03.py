""" Lab 3: Recursion """

LAB_SOURCE_FILE = "lab03.py"


# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3


def f91(n):
    """Takes a number n and returns n - 10 when n > 100,
    returns f91(f91(n + 11)) when n ≤ 100.

    >>> f91(1)
    91
    >>> f91(2)
    91
    >>> f91(100)
    91
    """
    "*** YOUR CODE HERE ***"
    if(n>100):
        return n-10
    else:
        return f91(f91(n + 11))
    

def is_monotone(n):
    """Returns whether n has monotone digits.
    Implement using recursion!

    >>> is_monotone(22000130)
    False
    >>> is_monotone(1234)
    True
    >>> is_monotone(24555)
    True
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'is_monotone', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return True
    else:
        return is_monotone(n//10) and  (n%10>=(n%100)//10)
       
    

def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(10)
    89
    """
    "*** YOUR CODE HERE ***"
    return count_stair_ways(n-1) + count_stair_ways(n-2) if n > 1 else 1

def count_k(n, k):
    """Counts the number of paths to climb up a flight of n stairs,
    taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    >>> count_k(3, 5) # Take no more than 3 steps
    4
    """
    "*** YOUR CODE HERE ***"

def count_k(n, k):
    """Counts the number of paths to climb up a flight of n stairs,
    taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    >>> count_k(3, 5) # Take no more than 3 steps
    4
    """
    "*** YOUR CODE HERE ***"
    if(k>n):
        k=n
    if n == 0:
        return 1  # One way to stay at the ground
    elif n < 0:
        return 0  # No ways to reach a negative step

    # Recursive case: sum the ways to get to the previous k steps
    total_ways = 0
    for i in range(1, k + 1):
        total_ways += count_k(n - i, k)

    return total_ways

    


    
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if(m==1 and n==1):
        return 1
    elif(m*n<=0):
        return 0
    else:
        return paths(m-1, n) + paths(m, n-1)

def max_subseq(n, l):
    """
    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    >>> max_subseq(12345, 66666)
    12345
    """
    "*** YOUR CODE HERE ***"
    str_n = str(n)

    if l>=len(str_n):
        return n
    if l==0:
        return 0

    def get_subsequences_of_length(s, l):
        # Helper function to recursively generate subsequences of length `l`
        def helper(current, index):
            if len(current) == l:
                subsequences.append(current)
                return
            # Generate subsequences by choosing the next character
            for i in range(index, len(s)):
                helper(current + s[i], i + 1)

        subsequences = []
        helper("", 0)
        return subsequences
    listn=get_subsequences_of_length(str_n, l)
    return max(int(i) for i in listn)
'''
    def getWeiShu(n):
        count=0
        while(n>0):
            n=n//10
            count+=1    
        return count
    count = getWeiShu(n)
    if (l==1):
        max=0
        while(n>0):
            if(n%10>max):
                max=n%10
            n=n//10
        return max
    elif(count==l):
        return n
    else:
        last_digit=n%10
        a=max_subseq(n//10, l-1)*10+last_digit
        b=max_subseq(n//10, l)
        return a if a>b else b
'''
'''
    def getWeiShu(n):
        if (n < 10):
            return 1
        else:
            return getWeiShu(n // 10) + 1
    count=getWeiShu(n)
    if(l>=count):
        return n

    first_digit = n // (10)**(count - 1)
    second_digit = (n //(10**(count -2)))%10
    if(first_digit > second_digit ):
        return max_subseq(first_digit*(10**(count-2))+n%((10)**(count -2)), l)
    else:
        return max_subseq(n%((10)**(count -1)), l)
'''
    

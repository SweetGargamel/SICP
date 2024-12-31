""" Homework 5: Nonlocal and Generators"""

from ADT import tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    Incorrect_password = []
    uncorrectTimes=0
    def withdraw(withdrawMoney,pwd):
        nonlocal uncorrectTimes
        if uncorrectTimes==3:
            return "Your account is locked. Attempts: ['{}', '{}', '{}']".format(Incorrect_password[0], Incorrect_password[1], Incorrect_password[2])
             
        if pwd!=password:
            uncorrectTimes=uncorrectTimes+1
            Incorrect_password.append(pwd)
            return 'Incorrect password'
            return 
        nonlocal balance
        if balance<withdrawMoney:
            return 'Insufficient funds'
        else:
            balance=balance-withdrawMoney
            return balance
    return withdraw

def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    returned=withdraw(0, old_pass)
    if type(returned)==int :
        def new_withdraw(amount, pwd):
            if pwd==new_pass:
                return withdraw(amount, old_pass)
            else:
                return withdraw(amount, pwd)
        return new_withdraw
    else:
        return  returned


def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of all elements in seq. The permutations could be yielded in any order.



    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"


    seq=list(seq)
    if len(seq) <= 1:
        yield seq
    else:
        # subseqs = list(permutations(seq[1:]))
        # for subseq in subseqs:
        #     for index in range(len(subseq)):
        #         print(type(subseq[:index] + seq[:1] + subseq[index:]))
        #         yield subseq[:index] + seq[:1] + subseq[index:]
        #     yield subseq + seq[:1]


        subseqs = list(permutations(seq[1:]))
        for subseq in subseqs:
            for index in range(len(subseq)):
                # print(seq[0])
                newlist=subseq[:index] + seq[:1] + subseq[index:]
                yield newlist
            newlist=subseq + seq[:1]
            yield newlist






        # # subseqList=list(permutations(seq[1:]))
        # # for subseq in permutations(seq[1:]):
        # subseq=next(permutations(seq[1:]))
        #     # print(type(subseq))
        #     # print("打印内{}".format(subseq))
        # for index in range(len(subseq)):
        #     # print("dayinnei{}".format(subseq[:index] +[seq[0]]+ subseq[index:]))
        #     yield sum([subseq[:index] ,[seq[0]], subseq[index:]],[])
        # # print("打印外{}".format(subseq+[seq[0]]))
        # yield sum([subseq, [seq[0]]],[])


def two_sum_pairs(target, pairs):
    """Return True if there is a pair in pairs that sum to target."""
    for i, j in pairs:
        if i + j == target:
            return True
    return False


def pairs(lst):
    """Yield the search space for two_sum_pairs.

    >>> two_sum_pairs(1, pairs([1, 3, 3, 4, 4]))
    False
    >>> two_sum_pairs(8, pairs([1, 3, 3, 4, 4]))
    True
    >>> lst = [1, 3, 3, 4, 4]
    >>> plst = pairs(lst)
    >>> n, pn = len(lst), len(list(plst))
    >>> n * (n - 1) / 2 == pn
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            yield (lst[i], lst[j])  


def two_sum_list(target, lst):
    """Return True if there are two different elements in lst that sum to target.

    >>> two_sum_list(1, [1, 3, 3, 4, 4])
    False
    >>> two_sum_list(8, [1, 3, 3, 4, 4])
    True
    """
    visited = []
    for val in lst:
        "*** YOUR CODE HERE ***"
        lst.pop(0)
        if (target-val) in lst:
            return True

    return False


def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    >>> k = tree(5, [tree(7, [tree(2)]), tree(8, [tree(3), tree(4)]), tree(5, [tree(4), tree(2)])])
    >>> v = tree('Go', [tree('C', [tree('C')]), tree('A', [tree('S'), tree(6)]), tree('L', [tree(1), tree('A')])])

    >>> t = tree(1,[tree(2,[tree(2),tree(2)]),tree(2),tree(2,[tree(2,[tree(2)])])])
    >>> t1=tree(1,[tree(2,[tree(4),tree(7)]),tree(3),tree(5,[tree(6,[tree(8)])])])  

    >>> type(lookups(k, 4))
    <class 'generator'>
    >>> sorted([f(v) for f in lookups(k, 2)])
    ['A', 'C']
    >>> sorted([f(v) for f in lookups(k, 3)])
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    "*** YOUR CODE HERE ***"

    def dfs(p, path):
        def func(v):
            u = v
            for x in path:
                u = branches(u)[x]
            return label(u)
            
        if label(p) == key:
            yield func
            
        for i in range(len(branches(p))):
            # path.append(i)
            yield from dfs(branches(p)[i], path + [i])
            # path.pop()

    return dfs(k, [])




# 自己的对的程序
    # def getapath(k_tree, key_wanted, former_path):
    #     if label(k_tree) == key_wanted:
    #         yield former_path
    #     if is_leaf(k_tree):
    #         return
    #     for i in range(len(branches(k_tree))):
    #         yield from getapath(branches(k_tree)[i], key_wanted, former_path + [i])

    # paths = list(getapath(k, key, []))

    # def helper(v, path):
    #     if len(path) == 0:
    #         return label(v)

    #     else:
    #         i=path[0]
    #         return helper(branches(v)[i], path[1:])
    # count =-1
    # for i in range(len(paths)):
    #     def finder(v):
    #         nonlocal count
    #         count += 1
    #         return helper(v,paths[count])
    #     yield finder




    # if label(k)==key:
    #     def finder(v):
    #         return label(v)
    #     yield finder

    # for b in branches(k):
    #     for f in lookups(b, key):
    #         def finder(v):
    #             return f(branches(v)[branches(k).index(b)])
    #         yield finder
    
##########################
# Just for fun Questions #
##########################


def remainders_generator(m):
    """Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"


def starting_from(start):
    """Yields natural numbers starting from start.

    >>> sf = starting_from(0)
    >>> [next(sf) for _ in range(10)] = list(range(10))
    """
    "*** YOUR CODE HERE ***"


def sieve(t):
    """Suppose the smallest number from t is p, sieves out all the
    numbers that can be divided by p (except p itself) and yields
    the reset of them.

    >>> list(sieve(iter([3, 4, 5, 6, 7, 8, 9])))
    [3, 4, 5, 7]
    >>> list(sieve(iter([2, 3, 4, 5, 6, 7, 8, 9])))
    [2, 3, 5, 7]
    >>> list(sieve(iter([1, 2, 3, 4, 5])))
    [1]
    """
    "*** YOUR CODE HERE ***"

def primes():
    """Yields all the prime numbers.

    >>> p = primes()
    >>> [next(p) for _ in range(10)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    "*** YOUR CODE HERE ***"

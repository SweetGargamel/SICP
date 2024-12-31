""" Homework 4: Data Abstraction and Trees"""

from ADT import tree, label, branches, is_leaf, print_tree, copy_tree


#####################
# Required Problems #
#####################

# Problem 1
def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    "*** YOUR CODE HERE ***"
    return [[lst1[i], lst2[i]] for i in range(len(lst1))]


# Problem 2
# The constructor and selectors of the arm
def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]


def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'


def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]
    

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]


def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]


def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'


def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]


def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


# Problem 2.1
def planet(size):
    """Construct a planet of some size.

    >>> planet(5)
    ['planet', 5]
    """
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ['planet', size] 


def size(w):
    """Select the size of a planet.

    >>> p = planet(5)
    >>> size(p)
    5
    """
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

# examples and usage
def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a planet or mobile.
    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return size(m)
    else: 
        # return total_weight(left(m)) + total_weight(right(m))
        return total_weight(end(left(m)))+total_weight(end(right(m)))

# Problem 2.2
def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    """
    assert is_mobile(m)
    "*** YOUR CODE HERE ***"
    left_size=0
    rigth_size=0
    flag=True
    if(is_planet(end(left(m)))):
        left_size=size(end(left(m)))
    else:
        flag=balanced(end(left(m))) and flag
        left_size=total_weight(end(left(m)))
    if(is_planet(end(right(m)))):
        rigth_size=size(end(right(m))) 
    else:
        flag= balanced(end(right(m)) ) and flag
        
        rigth_size=total_weight(end(right(m)))
    if left_size*length(left(m))!=rigth_size*length(right(m)):
      flag=False
    return flag
        
    
# Problem 2.3
def totals_tree(m):
    """Return a tree representing the mobile/planet with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    assert is_mobile(m) or is_planet(m)
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return tree(size(m))
    else:
      return tree(total_weight(m),[totals_tree(end(left(m))),totals_tree(end(right(m)))])  
# Problem 3.1
def add_trees(t1, t2):
    """
    >>> numbers = tree("hello",
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree("8")])])
    >>> print_tree(add_trees(numbers, numbers))
    hellohello
      4
        6
        8
      10
        12
          14
        88
    >>> print_tree(add_trees(tree("h"), tree("3", [tree(4), tree(5)])))
    h3
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree("4")])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    
    """
    "*** YOUR CODE HERE ***"
    def deep(l):
        if type(l)!=list:
            return l
        else:
            return [deep(i) for i in l]	
    if is_leaf(t1) and is_leaf(t2):
        return tree(deep(label(t1))+deep(label(t2)))
    elif is_leaf(t1):
        return tree(deep(label(t1))+deep(label(t2)),[copy_tree(b) for b in branches(t2)])
    elif is_leaf(t2):
        return tree(deep(label(t1))+deep(label(t2)),[copy_tree(b) for b in branches(t1)])
    else:
        if len(branches(t1))==len(branches(t2)):

          newBranchList=[add_trees(branches(t1)[i],branches(t2)[i]) for i in range(len(branches(t1)))]
          return tree(deep(label(t1))+deep(label(t2)),newBranchList)
        elif len(branches(t1))>len(branches(t2)) :

          newBranchList=[add_trees(branches(t1)[i],branches(t2)[i]) for i in range(len(branches(t2)))]
          
          newBranchList+= [copy_tree(b) for b in branches(t1)[len(branches(t2)):]]
          return tree(deep(label(t1))+deep(label(t2)),newBranchList)
        else:

          newBranchList=[add_trees(branches(t1)[i],branches(t2)[i]) for i in range(len(branches(t1)))]
          
          newBranchList+= [copy_tree(b) for b in branches(t2)[len(branches(t1)):]]
          return tree(deep(label(t1))+deep(label(t2)),newBranchList)  
                



# Problem 3.2
def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])

    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
      return 1 if label(t)>=n else 0
    else:
      return sum([bigpath(b,n-label(t)) for b in branches(t)]) + (1 if label(t)>=n else 0)
    

# Problem 3.3
def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
      return 1 if label(t)>=n else 0
    else:
        return sum([bigger_path(b,n) for b in branches(t)]) + bigpath(t,n)


# Problem 3.4
def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y

    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)==word
    elif len(word)==1:
        return label(t)==word
    else:
        listFlag=[has_path(b,word[1:]) for b in branches(t) if label(t)==word[0]]
        return any(listFlag)


##########################
# Just for fun Questions #
##########################

# Problem 4
def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"

def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')


def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')

def has_path_fold(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path_fold(greetings, 'h')
    True
    >>> has_path_fold(greetings, 'i')
    False
    >>> has_path_fold(greetings, 'hi')
    True
    >>> has_path_fold(greetings, 'hello')
    True
    >>> has_path_fold(greetings, 'hey')
    True
    >>> has_path_fold(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')

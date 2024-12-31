# Demo 1

5 * 2
5 ** 2 # Power operator
5 / 2 # True division, returns a number with a decimal component
5 // 2 # Floor division, rounds down to next smallest number
5 // (-2)



# Calculate circumference, area, volume of Earth
2 * 3.14159 * 3958.8 
3.14159 * 3958.8 * 3958.8
(4 / 3) * 3.141509 * 3958.8 * 3958.8 * 3958.8


# Assignment & importing names
radius = 3958.8
radius
radius = 1
radius
2 * 3.14159 * radius
pi
pi = 3.14
pi


import builtins

builtins.max(3, 5)

max = min
max(3, 5)
builtins.max(3, 5)


from math import pi
pi
radius = 3958.8
2 * radius * pi
(4 / 3) * pi * (radius ** 3)

# Non-primitive expressions & assignment
circ = 2 * pi * radius
circ
vol = (4 / 3) * pi * (radius ** 3)
vol
vol / 2
circ * 6

# "Out of synch" assignment
radius = 1
radius
circ
circ = 2 * pi * radius
circ
vol, circ = (4/3) * pi * (radius ** 3), 2 * pi * radius
vol
circ

vol = (4/3) * pi * (radius ** 3)
circ = 2 * pi * radius

x = 0
x = x + 1
x = x + 1

x, y = x+1, x+2
x = 2
x = x + 1
y = x + 2


radius
# Saving past assingments
mars_radius = radius
mars_radius
radius = 43441
mars_radius
radius



# Demo 2
radius = 10
vol = (4 / 3) * pi * (radius ** 3)
vol
radius = 20
vol = (4 / 3) * pi * (radius ** 3)


def power4(x):
    temp = x * x
    return temp * temp

power4(5)

def volume(r):
    # return (4 / 3) * pi * (r ** 3)
    return (4 / 3) * pi * r * r * r

def volume(r):
    (4 / 3) * pi * (r ** 3)

volume
volume(10)
volume(20)
radius
volume(radius)
radius = 10
volume(radius)

def v(r):
    (4 / 3) * pi * (r ** 3)

def sayHello(name):
    print("Hello "+name)



def vol_ratio(r1, r2):
    return volume(r1) / volume(r2)

vol_ratio
vol_ratio(20, 10)
vol_ratio(43441, 2106)

f = vol_ratio
f(20, 10)
vol_ratio = 10
f
vol_ratio
f(20, 10)

def test(x):
    x = x + 1
    a = x + 1
    print(a)
    x = x * x
    return x

# print(a)

y = 3
def test(x, z):
    return x * x * y * z

x = test

x(3, 5)
x(4, 6)
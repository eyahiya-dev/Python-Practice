"""
There are three numeric types in Python:
* int
* float
* complex

"""

x = 1 #int
y = 3.5 #float
z = 1j #complex
m = -564 #int
print(type(m))
print(type(x))
print(type(y))
print(type(z))


# float type data
x = 35e3
y = 12E4
print(type(x))
print(type(y))

#complex type data
x = 3+5j
y = 10j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# data type conversion
o = 5
p = 2.6
q = -3j

a = float(o)
print(a)

b = int(p)
print(b)

c = complex(o)
print(c)

import random
print(random.randrange(1, 100))
print(random.randint(1,10000))

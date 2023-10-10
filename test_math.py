#Import math library
import math

#Round a number upward to its nearest integer
x = math.ceil(1.4)

#Round a number downward to its nearest integer
y = math.floor(1.4)

print(x)
print(y)

def test_1():
    assert x == 2, "Round a number upward to its nearest integer 2"

def tes_2():
    assert y == 1, "Round a number downward to its nearest integer 1"


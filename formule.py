from math import *

x=0.0
while x <= 1:
    print(x, round((x**2 + 3*x - 5)/(sqrt(x) + 2), 2))
    x = round(x + 0.1, 1)

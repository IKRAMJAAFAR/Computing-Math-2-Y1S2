import numpy as np
import matplotlib.pyplot as mat

def func(x):
    return abs(pow(x,2) - 1)


x = np.linspace(-3, 3, 100)
y = func(x)
fig, ax = mat.subplots()
mat.plot(x,y)


mat.ylabel("f(x)")
mat.xlabel("x")
mat.title("f(x) = |x^2 - 1|")
mat.axhline(color = 'black')
mat.axvline(color = 'black')

mat.show()
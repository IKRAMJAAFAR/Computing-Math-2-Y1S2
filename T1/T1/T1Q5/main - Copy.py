import matplotlib.pyplot as py
import numpy as num

x = num.linspace(0,200/4,1000)
y = 200 - 4*x

py.plot(x,y)
py.ylabel("Number of spaces can be rented (cm\u00b2)")
py.xlabel("Charge ($)")
py.axhline(color = 'black')
py.axvline(color = 'black')
py.title("Spaces against charge")

py.show()

# Slope= -4 = Number of spaces per charge
# x-intercept = 50 = The maximum of charge can be spent with 0 cm^2
# y-intercept = 200 = The minimum of charge can be spent with 200 cm^2
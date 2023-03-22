# set independent variable as width
# set dependent variable as the total cost

import numpy as num
import matplotlib.pyplot as py

def totalCost(x):
    length = x * 2
    height = 10/length/x
    areaBase = x*length
    areaSide = 2*height*(length + x)
    return 10*areaBase + 6*areaSide

print(totalCost(pow(6,1/3)))
width = num.linspace(1,150,100_000)
py.plot(width,totalCost(width))
py.title("Total cost to make the container based on the width")
py.ylabel("Total cost ($)")
py.xlabel("width (m)")
py.axhline(color = 'black')
py.axvline(color = 'black')

py.show()

#What can I see from the graph?
#As the width increase, the container becomes smaller
#Overall cheap?
#width increases exponentially with the total cost
#
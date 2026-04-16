#Python List
list1 = [[1.73, 1.68,2],[ 1.71, 1.89,3]]
#print(list1[1][:])

#Functions and Packages
list1 = [[1.73, 1.98,2],[ 1.71, 1.89,3]]
list2 =  ["height", 6.6, "weight", 50, "age", 23]
list3 = ["max", "nim"]

"""functions:
max, min, median,
len, sum, count,
upper, capitalize, lower,
len, help, reverse, remove, 
"""
    #round
numerical = 4.91232
#print(round(numerical, 1))

    #count
x = [5,10,15] + [2,4,6]
#print(x.count(x[0]))

    #max
#print(max(list2))

    #replace in list
replace = list3[1] = "min"
#print(list3)

    #replace in string
text = "john dave"
replace = text.replace("dave", "doe")
#print(replace)

    #index method
#print(list2.index("weight"))

    #append
append1 = list3.append("median")
#print(list3)


#Packages
import numpy as np
import math
from math import pi

lit = math.pi
#print(lit)

WeightxPi = 50 * pi
#print(str(WeightxPi))

#Numpy
weight = [65.4, 59.2, 63.6]
height = [1.73, 1.56, 1.71]

np_weight = np.array(weight)
np_height = np.array(height)

wl = np_weight / np_height ** 2 #Normal list/tuples cant do operatos with more than one value inside a variable
#print(wl)

#2D Numpy
np_2d = np.array([[1.2, 2.3], [3.3, 4.4]])
#print(np_2d[0][1])


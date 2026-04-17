import numpy as np

#Dictionaries
fruits = { 
    'apples':{'cost':3, 'units':100}, 
    'bananas':{'cost':1, 'units':80},
    'grapes':{'cost':5, 'units':500}
}
print(fruits["bananas"]['units'])

#Np basic statistics
    #np.ranmdom.normal
h  = np.random.normal(0, 2, 5)
#print(h)



#MatplotLib
import matplotlib.pyplot as plt

year = [2020, 2021, 2022, 2029]
pop = [1100, 1200, 1300, 1400]
age = [20, 35, 40, 50, 55, 60]

plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population')
plt.yticks([1100, 1200, 1300, 1400])
plt.xticks([2020, 2021, 2022, 2029], ['1.2k', '1.2k', '1.3k', '1.4k'])
plt.grid(True)

plt.show()

#plt.scatter(year, pop)
#plt.xscale('log') <- best for skewed data, it will add ** to every x value to see data better
#plt.show()

#plt.hist(age, bins = 20)
#plt.show()

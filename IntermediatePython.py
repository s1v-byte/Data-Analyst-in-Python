import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Dictionaries
fruits = { 
    'apples':{'cost':3, 'units':100}, 
    'bananas':{'cost':1, 'units':80},
    'grapes':{'cost':5, 'units':500}
}
#print(fruits["bananas"]['units'])

#Np basic statistics
    #np.ranmdom.normal
h  = np.random.normal(0, 2, 5)
#print(h)



#MatplotLib
"""import matplotlib.pyplot as plt

year = [2020, 2021, 2022, 2029]
pop = [1100, 1200, 1300, 1400]
age = [20, 35, 40, 50, 55, 60]

plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population')
plt.yticks([1100, 1200, 1300, 1400])
plt.xticks([2020, 2021, 2022, 2029], ['1.2k', '1.2k', '1.3k', '1.4k'])
plt.grid(True)"""

#plt.show()

#plt.scatter(year, pop)
#plt.xscale('log') <- best for skewed data, it will add ** to every x value to see data better
#plt.show()

#plt.hist(age, bins = 20)
#plt.show()

#DICTIONARIES
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

#print(europe.keys())
# Print out value that belongs to key 'norway'
#print(europe['norway'])

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
#print(europe['france'])
# Create sub-dictionary data
data = { 'capital': 'rome', 'population': 59.83 }
# Add data to europe under key 'italy'
europe['italy'] = data
#print(europe)

#PANDAS
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'],
            'drives_right': [True, False, False, False, True, True, True],
            'cars_per_cap': [809, 731, 588, 18, 200, 70, 45]}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
#print(cars)
#Access columns
#print(cars[["country", "drives_right"]])
#Access rows
#print(cars[0:4])
#Acess Both
#print(cars.loc[1:3], ["country", "drives_right"])

#NUMPY
# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
#print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
#print(np.logical_and(my_house < 11, your_house < 11))

#IF ELSE ELIF
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
"""if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")"""

#FILTERING PANDAS
#cars = pd.read_csv('cars.csv', index_col = 0)

# Create medium: observations with cars_per_cap between 100 and 500
#medium = cars[np.logical_and(cars["cars_per_cap"] > 100, cars["cars_per_cap"] < 500)]
#print(medium)
"""
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JPN           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True
"""

#LOOPS
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
  #print("correcting...")
  offset = offset - 1
  #print(offset)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    #print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1  
    #print(offset)

#FOR LOOPS
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
#for room, area in house:
    #print("the", room + " is " + str(area) + " sqm")

#cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
#for lab,row in cars.iterrows():
    #print(lab)
    #print(row)


# Adapt for loop
#for lab, row in cars.iterrows() :
    #print(lab,row['cars_per_cap'])

#Case Study: Hacker Statistics
# NumPy is imported, seed is set
seed = np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif 3 <= dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1,7)

# Print out dice and step
#print(dice, step)

#Random Walk
# NumPy is imported, seed is set

# Initialization
random_walk = [0]
"""
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)"""

"""# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()"""

# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends, bins = 10)
plt.show()
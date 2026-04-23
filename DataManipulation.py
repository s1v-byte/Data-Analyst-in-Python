import pandas as pd

#INTRODUCING DATAFRAMES
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

dict1 = pd.DataFrame(europe).T
"""print(dict1.keys())
print("columns:",dict1.columns)
print("values",dict1.values)
print("index", dict1.index)
print(dict1.head())"""

#SORTING AND SUBSETTING
"""print(dict1.sort_values("population", ascending=False))
print(dict1.sort_values(["capital","population"], ascending=[False, True]))"""

#Subsetting
"""print(dict1["population"])
print(dict1[["population","capital"]])
list1 = ["population", "capital"]
print(dict1[list1])
print(dict1[dict1["population"] > 50])
print(dict1[dict1["population"]==66.03])
is_46 = dict1["population"] == 46.77
is_madrid = dict1["capital"] == "madrid"
print(dict1[is_46 & is_madrid])
is_oslo_is_madrid = dict1["capital"].isin(["madrid", "oslo"])
print(dict1[is_oslo_is_madrid])"""

#New Columns
dict1["times_2_pop"] = dict1["population"] * 2
#print(dict1["times_2_pop"])

dict1["high_times_2_pop"] = dict1["times_2_pop"] > 100
#print(dict1.head())

#Aggregating DataFrames
# Print the head of the sales DataFrame
#print(dict1.head())

# Print the info about the sales DataFrame
#print(dict1.info())

# Print the mean of weekly_sales
#print(dict1["population"].mean())

# Print the median of weekly_sales
#print(dict1["population"].median())

#print(dict1["population"].cumsum())
#print(dict1["population"].cummax())

#Counting
dict1_count = dict1["population"].value_counts()
print(dict1_count)

dict1_count = dict1["population"].value_counts(normalize=True)#Percentage
print(dict1_count)

dict1_count = dict1["population"].value_counts(sort=True, normalize=True)#Percentage
print(dict1_count)
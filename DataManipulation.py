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
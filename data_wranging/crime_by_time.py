import pandas as pd

import os

def bin_assign(x):
    # print(x)
    return 1
df = pd.read_csv("SF Visulisation/Police_Department_Incidents_-_Previous_Year__2016_.csv")







df["Time"] = df["Time"].apply(lambda x: x.split(":")[0])
df = df.groupby(['Category', 'Time', "PdDistrict", "DayOfWeek"]).count()


df.reset_index(inplace = True)
df.rename(columns = {"IncidntNum": "Count"}, inplace = True)
df = df[["Category", "Time", "PdDistrict", "Count", "DayOfWeek"]]

df.to_csv("SF Visulisation/crime_by_time.csv")



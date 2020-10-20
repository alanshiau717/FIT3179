import pandas as pd

import os

df = pd.read_csv("SF Visulisation/Police_Department_Incidents_-_Previous_Year__2016_.csv")



df = df.groupby(['Category', 'DayOfWeek']).count()

df.reset_index(inplace = True)
df = df[['Category', 'DayOfWeek', 'IncidntNum']]
df.rename(columns = {"IncidntNum": "Count"}, inplace = True)

df.to_csv("SF Visulisation/crime_by_day.csv")
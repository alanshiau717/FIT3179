import pandas as pd

import os


def parse_resolution(res):
    if res == "NONE":
        return "Unresolved"
    else:
        return "Resolved"
df = pd.read_csv("SF Visulisation/Police_Department_Incidents_-_Previous_Year__2016_.csv")



df['Resolution'] = df['Resolution'].apply(lambda x: parse_resolution(x))
df = df.groupby(['PdDistrict', "Resolution"]).count()
df.reset_index(inplace = True)

df.rename(columns = {"IncidntNum": "Count"}, inplace = True)
df = df[["PdDistrict", "Resolution", "Count"]]


df.to_csv("SF Visulisation/diverging.csv")



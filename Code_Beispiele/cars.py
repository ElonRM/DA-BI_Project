import pandas as pd
import plotly.express as px

df = pd.DataFrame()
df2 = pd.DataFrame()
df.merge(df2, on = "manufacturer")
#df.merge(df2, left_on=["manufacturer", "mpg"], right_on=["maufacturer", "maxmpg"])
print(df[df["mpg"] == df["maxmpg"]])
df[df.groupby("manufacturer")['mpg'].transform(max) == df['mpg']][["manufacturer", "mpg", "name"]]
import pandas as pd
import missingno as msno

df = pd.read_parquet('/Users/timehmann/Library/Mobile Documents/com~apple~CloudDocs/Studium/Data_Science_Semester3/Data_Analytics_Business_Intelligence/Projekt/escooter_history_2022.parquet')

print(df)
print(msno.matrix(df))
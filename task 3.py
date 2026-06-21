#import libraries

import pandas as pd
#read the CSV file

df = pd.read_csv("input\student.csv")
print(df)
#handle missing values

df.fillna("N/A",inplace=True)
print(df)
#normalize column names

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
print(df.columns)
#convert date format

df["join_date"] = pd.to_datetime(df["join_date"].astype(str),format="mixed", errors="coerce",dayfirst=True)
print(df)
#save as excel

df.to_excel("output\student.xlsx",index=False)
print("Excel file created successfully!")


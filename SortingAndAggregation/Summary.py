#df["ColumnName"].mean()
#df["ColumnName"].sum()
#df["ColumnName"].max()

import pandas as pd

data={
    "Name":["Raj","Varun","Arpit"],
    "Age":[28,35,25],
    "Salary":[10000,20000,30000]
}
df = pd.DataFrame(data)
print(df["Salary"].mean())
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Salary"].sum())
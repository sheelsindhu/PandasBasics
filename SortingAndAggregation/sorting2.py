#sorting of multiple columns
# Syntex-->df.sort_values(by=["Column Name"],ascending=[False,True],inplace=True)
import pandas as pd

data={
    "Name":["Raj","Varun","Arpit"],
    "Age":[28,35,25],
    "Salary":[10000,20000,30000]
}
df = pd.DataFrame(data)
df.sort_values(by=["Age","Salary"], ascending=[True,False] ,inplace=True)
print(df)
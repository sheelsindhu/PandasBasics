#sorting 
# Syntex-->df.sort_values(by="Column Name",ascending=False,inplace=True)
import pandas as pd

data={
    "Name":["Raj","Varun","Arpit"],
    "Age":[28,35,25],
    "Salary":[23000,45000,21000]
}
df = pd.DataFrame(data)
df.sort_values(by="Age",ascending=True,inplace=True)
print(df)
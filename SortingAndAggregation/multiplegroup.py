import pandas as pd
# Create a sample DataFrame
data = {
    'Name': ['A', 'V', 'K', 'N', 'E', 'G'], 
    'Age': [26, 29, 30, 21, 26, 29],
    'Salary': [50000, 60000, 45000, 35000, 55000, 41000]
}
df= pd.DataFrame(data)
group=df.groupby(["Name","Age"])["Salary"].sum()
print(group)
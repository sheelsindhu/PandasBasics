#adding columns
import pandas as pd

emp={
    "Name":['Ram','Shyam','Mohan','Sita','Rahul','Geeta','Raj','Anita'],
    "Age":[26,25,27,24,28,29,30,31],
    "Salary":[30000,32000,35000,28000,40000,45000,50000,48000],
    "Performance_Score":[80,85,90,75,95,88,92,87]
}

df = pd.DataFrame(emp)
#print(df)

#adding column 
#SYNTEX: df["column_name"]= value/Data
# Add a column "Bonus"and give 10% of Salary 
#df["Bonum"]=df["Salary"]*0.1

#insert(loc,"Key",value) method 
df.insert(0, "EmpId", [121,122,123,124,125,126,1257,128])
print(df)

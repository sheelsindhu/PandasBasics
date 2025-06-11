#How to fill missing data with value
#method fillna(value,inplace=True)
import pandas as pd

emp={
    "Name":['Ram',None,'Mohan','Sita','Rahul','Geeta','Raj','Anita'],
    "Age":[26,None,27,24,28,29,30,31],
    "Salary":[30000,45666,35000,None,40000,45000,50000,48000],
    "Performance_Score":[None,70,90,75,95,88,92,87]
}
df = pd.DataFrame(emp)
print(df)
# df.fillna(0,inplace=True) #This is for all the columns and rows of data frame
df["Name"].fillna("A",inplace=True)  #This is only for Name Column
print("After filling NAN with Zero")
print(df)

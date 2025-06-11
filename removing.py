import pandas as pd

emp={
    "Name":['Ram','Shyam','Mohan','Sita','Rahul','Geeta','Raj','Anita'],
    "Age":[26,25,27,24,28,29,30,31],
    "Salary":[30000,32000,35000,28000,40000,45000,50000,48000],
    "Performance_Score":[80,85,90,75,95,88,92,87]
}

df = pd.DataFrame(emp)

print(df)
#remove coulmn 
#df.drop(columns=["columnname"],inplace=True) inPlace =True means direct delete from Data frame
print("After Droping the cloumns")

df.drop(columns=["Age",],inplace=True)

print(df)
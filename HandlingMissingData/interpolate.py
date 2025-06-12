#work with numeric data and look for pattern is required
import pandas as pd

emp={
    "Name":['Ram',"Ravi",'Mohan','Sita','Rahul','Geeta','Raj','Anita'],
    "Age":[26,None,27,24,28,29,30,31],
    "Salary":[30000,45666,35000,None,40000,45000,50000,48000],
    "Performance_Score":[None,70,90,75,95,88,92,87]
}
df = pd.DataFrame(emp)

# we have different type of interpolate method few of them are:
#  -linear
#  -polynomial
#  -time
df.interpolate(method="linear",axis=0,inplace=True)
print(df)
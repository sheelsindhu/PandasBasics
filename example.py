import pandas as pd

emp={
    "Name":['Ram','Shyam','Mohan','Sita','Rahul','Geeta','Raj','Anita'],
    "Age":[26,25,27,24,28,29,30,31],
    "Salary":[30000,32000,35000,28000,40000,45000,50000,48000],
    "Performance_Score":[80,85,90,75,95,88,92,87]
}
df = pd.DataFrame(emp)
#salary_col = df["Salary"] #single column  that will returm series
# multi_column= df[["Name","Salary","Age"]]
# print(multi_column)

#filtering on Rows this will give Boolean in reply
#salary_col = df["Salary"]>30000  # filtering  will return boolean 
#salary_col=df[df["Salary"]>30000] # will return data frame 
#salary_col = df[(df["Salary"]>30000) & (df['Age']>28)]
# print(salary_col)
df1 = df[(df["Salary"]>5000) | (df["Performance_Score"]>80)]
print(df1)
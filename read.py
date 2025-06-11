import pandas as pd

#df = pd.read_csv("sales_data_sample.csv",encoding="latin1")
#df = pd.read_excel("SampleSuperstore.xlsx")
#df = pd.read_json("sample_Data.json",orient="records")
#print(df)

dic={
    "name":["Ravi","Rohan","Ramesh","Raju","Rani","Tina","Rita"],
    "age":[23,24,25,26,27,28,29],
    "city":["Delhi","Mumbai","Chennai","Kolkata","Bangalore","Hyderabad","Pune"],
    "salary":[10000,15000,20000,25000,30000,35000,40000]
}
# with index
df1=pd.DataFrame(dic)
#print(df1)
print(df1.to_string(index=False))


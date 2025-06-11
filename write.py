import pandas as pd
# dic={
#     "name":["Ravi","Rohan","Ramesh","Raju","Rani","Tina","Rita"],
#     "age":[23,24,25,26,27,28,29],
#     "city":["Delhi","Mumbai","Chennai","Kolkata","Bangalore","Hyderabad","Pune"],
#     "salary":[10000,15000,20000,25000,30000,35000,40000]
# }

#df = pd.DataFrame(dic)
#df.to_csv("customdata.csv",index=False)
# try:
#     df.to_excel("customdata.xlsx",index=False)
# except Exception as e:
#     print(f"Error writing to Excel file: {e}")

#df.to_json("customdata.json",orient="records",lines=True)

df1 = pd.read_csv("sales_data_sample.csv",encoding="latin1")
#print(df1)
# print(df1.head())
# print(df1.tail())
# print(df1.info())
#print(df1.describe())
# shape and columns are attribute not method
print(df1.shape)
print(df1.columns)
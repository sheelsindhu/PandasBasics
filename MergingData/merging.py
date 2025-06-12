#pd.merge(df1,df2,on="columnName",how="type of joins")
#type of join=inner,cross,left,right,outer
import pandas as pd

#customer data
df_customer =pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "customer_name": ["Alice", "Bob", "Charlie", "David"]
})

df_orders = pd.DataFrame({
    "customer_id": [1, 2, 5, 4],
    "order_amount": [250, 150, 200, 300]
})

#df_merged=pd.merge(df_customer,df_orders,on="customer_id", how="inner")
#df_merged=pd.merge(df_customer,df_orders,on="customer_id", how="outer")
#df_merged=pd.merge(df_customer,df_orders,on="customer_id", how="left")
df_merged=pd.merge(df_customer,df_orders,on="customer_id", how="right")
print(df_merged)
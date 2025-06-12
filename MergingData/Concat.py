import pandas as pd
"""
it will be vertical as well as horizental concat

Syntex->pd.concat([df1,df2],axis=0, ignore_index=True)

"""
df_region1=pd.DataFrame({
    "CustomerID":[1,2],
    "Name":["Gopal","Krishna"]
})

df_region2=pd.DataFrame({
    "CustomerID":[3,4],
    "Name":["Ram","Shayam"]
})
#df_concat=pd.concat([df_region1,df_region2],ignore_index=True) #added vertically
df_concat=pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(df_concat)
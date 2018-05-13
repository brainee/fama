# %load fama.py
# import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_book_value=pd.read_csv("./book_value_per_share.csv",index_col=0)
df_market_cap=pd.read_csv("./market_cap.csv")
price_data=pd.read_csv("./price_data.csv")
print(df_book_value)

index_date=df_book_value.index
stocks=df_book_value.columns
format='%Y-%m-%d %H:%M:%S'
btm = pd.DataFrame(index=index_date,columns=stocks)

i=0
for stk in stocks:
    for date in index_date:
        i=i+1
        if i==1:
            print("type(stk),type(date)",type(stk),stk,type(date),date)
        else:
            pass
#         dt=date.strftime(format)    
#         print("dt",type(dt),dt)
        
        if hasattr(price_data[stk],date):
            if price_data[stk][date]!=0:
                btm[stk][date] = df_book_value[stk][date]/price_data[stk][date]
            else:
                btm[stk][date] = 0
        else:
#             print('hasattr error',stk,date,type(date))
            btm[stk][date]=0
            
btm

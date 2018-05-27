import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''numpy
np.nan
np.array([5] * len(df))
np.array([3] * 4, dtype='int32')
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))


'''

'''series
s = pd.Series([1,3,5,np.nan,6,8])
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()
s.str.lower()
np.exp(s)
s + s
type(s) ndarray
'''


'''dataframe pandas
df = pd.DataFrame(np.random.randn(10, 4))
df.mean()
df1.fillna(value=5)
pd.isnull(df1)
df1 = df.reindex(index=dates[0:4],columns=list(df.columns) + ['E'])
df1.dropna(how='any')
df2[df2 > 0] = -df2
df2 = df.copy()
df2[df2['E'].isin(['two', 'four'])]
df.apply(np.cumsum)
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
pd.merge(left, right, on='key')
df.append(s, ignore_index=True)
df.groupby('A').sum()
df.groupby(['A', 'B']).sum()
stacked = df2.stack()
stacked.unstack()
df.describe()

new_ts = ts.resample('5Min', how='sum')
ts_utc = ts.tz_localize('UTC')
ts_utc.tz_convert('US/Eastern')
ps = ts.to_period()
ps.to_timestamp()
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
df['grade'] = df['raw_grade'].astype('category', ordered=True)
df['grade'].cat.categories = ['very good', 'good', 'very bad']
df['grade'] = df['grade'].cat.set_categories(['very bad', 'bad', 'medium', 'good', 'very good'])
df.head()
'''

'''pandas
pd.date_range('1/1/2012', periods=100, freq='S')
pd.date_range('20130101', periods=6)
np.random.randint(0, 500, len(rng))
iris = pd.read_csv('data/iris.data')

import pandas as pd
from six import BytesIO
body = get_file('day_px.csv')
    data=pd.read_csv(BytesIO(body))
    logger.info(data)

'''


'''json
import json
data = json.loads(jsonStr)
#a_js = json.dumps(data)　　　　#将python格式转化为json格式　
'''

'''
index=pd.date_range('1/1/2000',periods=1000)
df = pd.DataFrame(np.random.randn(1000, 4), index=index, columns=['A', 'B', 'C', 'D'])
df=df.cumsum();
# df.plot();
plt.figure;df.plot();plt.legend(loc='best')

import datetime  #倒入一个datetime model
# get_price('000001.XSHE',start_date='2015-04-01',end_date=datetime.datetime.now())

rng=range(1, 11)
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.iteritems()]
'''


'''
np.where(np.isnan(df))
np.where(np.isnan(df))[0] # 选出tuple里面的第一个元素，也就是行号
df.index[np.where(np.isnan(df))[0]]
df.columns[np.where(np.isnan(df))[1]]


'''

'''
df_book_value.to_csv("data/book_value_per_share.csv")
df_market_cap.to_csv("data/market_cap.csv")
price_data.to_csv("data/price_data.csv")
df=pd.read_csv("./dp_price_data2.csv")
print(df)
'''


df_book_value=pd.read_csv("./book_value_per_share.csv")
df_market_cap=pd.read_csv("./market_cap.csv")
price_data=pd.read_csv("./price_data.csv")
print(df_book_value)

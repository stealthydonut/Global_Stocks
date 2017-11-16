import urllib
import re
import json
import csv
import pandas as pd
import datetime
###########################################
#Extract minute by minute bloomberg prices#
###########################################
htmltext = urllib.urlopen(" http://www.bloomberg.com/markets/chart/data/1D/AAPL:US")           
data = json.load(htmltext)
datapoints = data["data_values"]
labels=['time','price']
df = pd.DataFrame(datapoints, columns=labels)
labels=['time','price']
df['UNIXTIME'] = pd.to_datetime(df['time'], unit='ms')
df['ind']=df.index
df['TICKER']='AAPL:US'
###############################
#Get the open, close, high, low
###############################
dfmax=df['price'].max()
dfmin=df['price'].min()
dfmaxtime=df['UNIXTIME'].max()
dfmintime=df['UNIXTIME'].min() 
###########
#High price
###########
high=df[df['price']==dfmax]
high['HIGH']=high['price']
high['DATE'] = high['UNIXTIME'].dt.strftime("%x")
del high['time']
del high['ind']
del high['price']
del high['UNIXTIME']
###########
#Low price
###########
low=df[df['price']==dfmin]
low['LOW']=low['price']
low['DATE'] = low['UNIXTIME'].dt.strftime("%x")
del low['time']
del low['ind']
del low['price']
del low['UNIXTIME']
###########
#Open Price
###########
openpr=df[df['UNIXTIME']==dfmaxtime]
openpr['OPEN']=openpr['price']
openpr['DATE'] = openpr['UNIXTIME'].dt.strftime("%x")
del openpr['time']
del openpr['ind']
del openpr['price']
del openpr['UNIXTIME']
#Close Price
close=df[df['UNIXTIME']==dfmaxtime]
close['CLOSE']=close['price']
close['DATE'] = close['UNIXTIME'].dt.strftime("%x")
del close['time']
del close['ind']
del close['price']
del close['UNIXTIME']
opcl=pd.merge(close, openpr, how='outer', left_on=('TICKER','DATE'), right_on=('TICKER','DATE'))
opclhi=pd.merge(high, opcl, how='outer', left_on=('TICKER','DATE'), right_on=('TICKER','DATE'))
opclhilo=pd.merge(low, opclhi, how='outer', left_on=('TICKER','DATE'), right_on=('TICKER','DATE'))
record=opclhilo[['DATE','TICKER','OPEN','HIGH','LOW','CLOSE']]
record_gold=record.drop_duplicates(['DATE','TICKER'], keep='last')


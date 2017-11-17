import pandas as pd
import requests
from pandas.compat import StringIO
import StringIO
import datetime
import ast
import itertools
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO as stio
else:
    from io import StringIO as stio

datevar=pd.to_datetime('today')
################################################
#Get the list of Canadian Tickers from Bloomberg
################################################
from google.cloud import storage
client = storage.Client()
bucket = client.get_bucket('bloomberg')
# Then do other things...
blob = bucket.get_blob('cn_ticker.csv')
content = blob.download_as_string()
#Because the pandas dataframe can only read from buffers or files, we need to take the string and put it into a buffer
inMemoryFile = StringIO.StringIO()
inMemoryFile.write(content)
#When you buffer, the "cursor" is at the end, and when you read it, the starting position is at the end and it will not pick up anything
inMemoryFile.seek(0)
#Note - anytime you read from a buffer you need to seek so it starts at the beginning
#The low memory false exists because there was a lot of data
cnticker=pd.read_csv(inMemoryFile, low_memory=False)
df1=cnticker['Ticker']
df2=df1.values.T.tolist()
#strip out leading and trailing 0's
tickerlist = [x.strip(' ') for x in df2]  

tickerlist=('GOLD:CN','ABX:CN')

###########################################
#Extract minute by minute bloomberg prices#
###########################################
minute = pd.DataFrame()
goldrecord = pd.DataFrame()

for i in tickerlist:
    try:
        tick=''.join(i)
        text='http://www.bloomberg.com/markets/chart/data/1D/'
        link=text+tick
        htmltext = urllib.urlopen(link)           
        data = json.load(htmltext)
        datapoints = data["data_values"]
        labels=['time','price']
        df = pd.DataFrame(datapoints, columns=labels)
        labels=['time','price']
        df['UNIXTIME'] = pd.to_datetime(df['time'], unit='ms')
        df['ind']=df.index
        df['TICKER']=tick    
        minute = minute.append(df, ignore_index=False)
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
        goldrecord = goldrecord.append(record_gold, ignore_index=False)        
    except:
       print i

    
    
##################################
#Put the dataset back into storage
##################################
from google.cloud import storage
client = storage.Client()
bucket2 = client.get_bucket('stagingarea')
df_out = pd.DataFrame(goldrecord)
df_out.to_csv('daily.csv', index=False)
blob2 = bucket2.blob('daily.csv')
blob2.upload_from_filename('daily.csv')

##################################
#Put the dataset back into storage
##################################
from google.cloud import storage
client = storage.Client()
bucket2 = client.get_bucket('stagingarea')
df_out = pd.DataFrame(minute)
df_out.to_csv('minute.csv', index=False)
blob2 = bucket2.blob('minute.csv')
blob2.upload_from_filename('minute.csv')

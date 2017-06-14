#This program will get the historical data for a number of tickers
import urllib
import pandas as pd
import numpy as np
import StringIO
import datetime
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO as stio
else:
    from io import StringIO as stio

#Get the data from google cloud storage
from google.cloud import storage
client = storage.Client()
bucket = client.get_bucket('mastfiles')
# Then do other things...
blob = bucket.get_blob('ticker_listUS_test.csv')
content = blob.download_as_string()
#Because the pandas dataframe can only read from buffers or files, we need to take the string and put it into a buffer
inMemoryFile = StringIO.StringIO()
inMemoryFile.write(content)
#When you buffer, the "cursor" is at the end, and when you read it, the starting position is at the end and it will not pick up anything
inMemoryFile.seek(0)
#Note - anytime you read from a buffer you need to seek so it starts at the beginning
#The low memory false exists because there was a lot of data
df=pd.read_csv(inMemoryFile, low_memory=False)
df1=df['google symbol']
df2=df1.values.T.tolist()
#strip out leading and trailing 0's
df2 = [x.strip(' ') for x in df2]    
    
    
#Get todays date
year = datetime.date.today().year
day = datetime.date.today().day
#Month
month = datetime.datetime.now()
month2=month.strftime('%B')
myfile = ''
bigdata = pd.DataFrame()

for i in df2:
    try:#Develop the text string that can get all the data
        stringone='https://www.google.com/finance/historical?output=csv&q='
        ticker=''.join([i])
        startdate='&startdate=May+22%2C+2010'
        enddate='&enddate='+str(month2)+'+'+str(day)+'%2C+'+str(year)
        text2=stringone+ticker+startdate+enddate      
        data = pd.read_csv(text2)
        data.columns = ['Date','Open','High','Low','Close','Volume']
        data['ticker']= i
        #need to convert this file so can read the date
        data['date']=pd.to_datetime(data['Date'], errors='coerce')
        data.sort_values('date',ascending=True, inplace=True)
        data['close_lag1']=data['Close'].shift(1)
        data['changepos']=np.where(data['Close']>data['close_lag1'], 1, 0)
        data['changeneg']=np.where(data['Close']<data['close_lag1'], 1, 0)
        data['changenone']=np.where(data['Close']==data['close_lag1'], 1, 0)
        data['High']=pd.to_numeric(data['High'], errors='coerce')
        data['Low']=pd.to_numeric(data['Low'], errors='coerce')
        data['Open']=pd.to_numeric(data['Open'], errors='coerce')
        data['Volume']=pd.to_numeric(data['Volume'], errors='coerce')
        bigdata = bigdata.append(data, ignore_index=False)
    except:
        print i
        print("Unexpected error:", sys.exc_info()[0])
        
        
#Put the dataset back into storage
bucket2 = client.get_bucket('stagingarea')
df_out = pd.DataFrame(bigdata)
df_out.to_csv('closing_prices_histUS.csv', index=False)
blob2 = bucket2.blob('closing_prices_histUS.csv')
blob2.upload_from_filename('closing_prices_histUS.csv')

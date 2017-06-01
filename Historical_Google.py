#This program will get the historical data for a number of tickers
import urllib
import pandas as pd
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
blob = bucket.get_blob('ticker_listUS.csv')
content = blob.download_as_string()
#Because the pandas dataframe can only read from buffers or files, we need to take the string and put it into a buffer
inMemoryFile = StringIO.StringIO()
inMemoryFile.write(content)
#When you buffer, the "cursor" is at the end, and when you read it, the starting position is at the end and it will not pick up anything
inMemoryFile.seek(0)
#Note - anytime you read from a buffer you need to seek so it starts at the beginning
#The low memory false exists because there was a lot of data
df=pd.read_csv(inMemoryFile, low_memory=False)
df1=df['Symbol']
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
        startdate='&startdate=May+22%2C+2015'
        enddate='&enddate='+str(month2)+'+'+str(day)+'%2C+'+str(year)
        text2=stringone+ticker+startdate+enddate      
        data = pd.read_csv(text2)
        data['ticker']= i
        bigdata = bigdata.append(data, ignore_index=False)
    except:
        print i

        
bigdata.columns = [['Date', 'Open','High','Low','Close','Volume', 'ticker']]
        
        
        
#Put the dataset back into storage
bucket2 = client.get_bucket('mastfiles')
df_out = pd.DataFrame(bigdata)
df_out.to_csv('closing_prices_hist.csv', index=False)
blob2 = bucket2.blob('closing_prices_hist.csv')
blob2.upload_from_filename('closing_prices_hist.csv')

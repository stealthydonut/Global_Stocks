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

myfile = ''
bigdata = pd.DataFrame()

myfile = ''
for i in df2:
    try:#Develop the text string that can get all the data
        start="http://finance.yahoo.com/d/quotes.csv?s="
        #date,Float Shares,Day's Low,Day's High,Open,Previous Close,Change,Volume,Name,Ticker,52 Low, 52 High,Dividend Share, Volume
        #end="&f=d1f6ghopc1vns"
        #date,Float ,Name,Ticker
        end="&f=d1f6s7oc1pghnsjkdk5j6rv"
        str1 = ''.join([i])
        text2=start+str1+end    
        #Get the data from the yahoo api
        link=text2
        f = urllib.urlopen(link)
        myfile += f.readline()
    except:
        print i

        
TESTDATA=stio(myfile)

daily_prices = pd.read_csv(TESTDATA, sep=",", names=['date','Float Shares','Short Ratio','Open','Change','Previous Close','Low','High','Name','Ticker','52 Low','52 High','Dividend','Per change 52 H','Per change 52 L','PE Ratio','Volume'])
daily_prices['Div Yield']=(daily_prices['Dividend']/daily_prices['Previous Close'])*100      

bigdata=pd.merge(daily_prices, df, left_on='Ticker', right_on='Symbol')

from google.cloud import storage
client = storage.Client()
bucket = client.get_bucket('oiltrade')
# Then do other things...
blob = bucket.get_blob('all_alligator.csv')
content = blob.download_as_string()
inMemoryFile = StringIO.StringIO()
inMemoryFile.write(content)
#When you buffer, the "cursor" is at the end, and when you read it, the starting position is at the end and it will not pick up anything
inMemoryFile.seek(0)

daily_prices2 = pd.read_csv(inMemoryFile, sep=",", header=1, names=['date','Float Shares','Short Ratio','Open','Change','Previous Close','Low','High','Name','Ticker','52 Low','52 High','Dividend','Per change 52 H','Per change 52 L','PE Ratio','Div Yield','IPOyear','Index','LastSale','MarketCap','Mkt Cap','Name_y','Sector','industry','insert date','var','zero','symbol2','exchange','google symbol','Volume'])

bigdata2 = daily_prices2.append(bigdata, ignore_index=True)



#Put the dataset back into storage
from google.cloud import storage
client = storage.Client()
bucket2 = client.get_bucket('oiltrade')
df_out = pd.DataFrame(bigdata2)
df_out.to_csv('all_alligator.csv', index=False)
blob2 = bucket2.blob('all_alligator.csv')
blob2.upload_from_filename('all_alligator.csv')

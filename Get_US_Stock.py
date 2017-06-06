#The objective of this script is to identify the tickers on the major exchanges
#These datasets will be used for data extraction purposes

import urllib
import pandas as pd
#sudo -H pip install six==1.10.0
#sudo -H pip install html5lib==1.0b8
#sudo pip install beautifulsoup4
import html5lib
#import beautifulsoup4
import datetime
import StringIO

######################################
#Download the files from the exchanges
######################################

dls = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
urllib.urlretrieve(dls, "test.xls")
data1 = pd.read_csv('test.xls')
data1['Index']='nasdaq'

dls = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
urllib.urlretrieve(dls, "test.xls")
data2 = pd.read_csv('test.xls')
data2['Index']='nyse'

dls = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"
urllib.urlretrieve(dls, "test.xls")
data3 = pd.read_csv('test.xls')
data3['Index']='amex'

###################################
#Set the data on top of one another
###################################
set1 = data1.append(data2, ignore_index=True)
ticker = data3.append(set1, ignore_index=True) 

###############################################
#Create a timestamp to insert on a master table
###############################################

from datetime import datetime, timedelta
insert = datetime.today()

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day 

stamp=str(month)+'/'+str(day)+'/'+str(year)

ticker['insert date'] = stamp

##################################
#Clean up the market captilization 
##################################
ticker['char']=ticker['MarketCap'].str[-1:]
ticker['var'] = ticker.loc[ticker['MarketCap'].index, 'MarketCap'].map(lambda x: x.replace('$','').replace('.','').replace('B','').replace('M','').replace('n/a',''))
tickerB = ticker[ticker['char'] == 'B']
tickerB['zero']= '000000000'
tickerB['Mkt Cap']=tickerB['var']+tickerB['zero']
tickerB['Mkt Cap']=pd.to_numeric(tickerB['Mkt Cap'], errors='coerce')
tickerB['LastSale']=pd.to_numeric(tickerB['LastSale'], errors='coerce')
tickerB['Shares']=tickerB['Mkt Cap']/tickerB['LastSale']
tickerB['Shares'] = tickerB['Shares'].round(0).astype(int)
tickerM = ticker[ticker['char'] == 'M']
tickerM['zero']= '000000'
tickerM['Mkt Cap']=tickerM['var']+tickerM['zero']
tickerM['Mkt Cap']=pd.to_numeric(tickerM['Mkt Cap'], errors='coerce')
tickerM['LastSale']=pd.to_numeric(tickerM['LastSale'], errors='coerce')
tickerM['Shares']=tickerM['Mkt Cap']/tickerM['LastSale']
tickerM['Shares'] = tickerM['Shares'].round(0).astype(int)
tickera = ticker[ticker['char'] == 'a']

file1 = tickerM.append(tickerB, ignore_index=True)
file2 = tickera.append(file1, ignore_index=True)

##################################
#Begin to create the google ticker
##################################

#Replace the tickers with the google symbol
file2['symbol2'] = file2.loc[file2['Symbol'].index, 'Symbol'].map(lambda x: x.replace('^','-').replace('.WS',''))
#Get the correct google symbol
tickeramex = file2[file2['Index'] == 'amex']
tickeramex['exchange']='NYSEMKT:'
tickeramex['google symbol']=tickeramex['exchange']+tickeramex['symbol2']
tickernas = file2[file2['Index'] == 'nasdaq']
tickernas['exchange']='NASDAQ:'
tickernas['google symbol']=tickernas['exchange']+tickernas['symbol2']
tickernyse = file2[file2['Index'] == 'nyse']
tickernyse['exchange']='NYSEMKT:'
tickernyse['google symbol']=tickernyse['exchange']+tickernyse['symbol2']

file3 = tickernas.append(tickernyse, ignore_index=True)
ticker_gold = tickeramex.append(file3, ignore_index=True)

#############################
#Generate the Historical File
#############################
from google.cloud import storage
client = storage.Client()
bucket = client.get_bucket('mastfiles')
# Then do other things...
blob = bucket.get_blob('ticker_listUS.csv')
content = blob.download_as_string()
inMemoryFile = StringIO.StringIO()
inMemoryFile.write(content)
inMemoryFile.seek(0)
prior_day=pd.read_csv(inMemoryFile, low_memory=False)

bigdata = prior_day.append(ticker_gold, ignore_index=True)

from google.cloud import storage
client = storage.Client()
bucket2 = client.get_bucket('historicalfiles')
df_out = pd.DataFrame(bigdata)
df_out.to_csv('ticker_listUS_historical.csv', index=False)
blob2 = bucket2.blob('ticker_listUS_historical.csv')
blob2.upload_from_filename('ticker_listUS_historical.csv')

##################################
#Export the file to google storage
##################################
from google.cloud import storage
client = storage.Client()
bucket2 = client.get_bucket('mastfiles')
df_out = pd.DataFrame(ticker)
df_out.to_csv('ticker_listUS.csv', index=False)
blob2 = bucket2.blob('ticker_listUS.csv')
blob2.upload_from_filename('ticker_listUS.csv')




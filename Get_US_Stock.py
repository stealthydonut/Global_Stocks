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

ticker['insert date'] = datetime.today()

##################################
#Clean up the market captilization 
##################################
#ticker['char']=ticker['MarketCap'].str[-1:]
#tickerB = ticker['char'] == 'B'

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




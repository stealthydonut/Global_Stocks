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

dls = "http://thecse.com/sites/default/files/documents/activity_summaries/CSE_Listed/CSE Stock List.xls"
urllib.urlretrieve(dls, "test.xls")
df = pd.read_excel('test.xls', skiprows=4)
df.columns = ['Company Name','Ticker','Currency','Industry','Date','Unknown1','Unknown2','CSE Specific FIGI','Unknown3']

df.__delitem__('Unknown1')
df.__delitem__('Unknown2')
df.__delitem__('Unknown3')

###############################################
#Create a timestamp to insert on a master table
###############################################

from datetime import datetime, timedelta
insert = datetime.today()

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day 

stamp=str(month)+'/'+str(day)+'/'+str(year)

df['insert date'] = stamp

##################################
#Export the file to google storage
##################################
from google.cloud import storage
client = storage.Client()
bucket2 = client.get_bucket('mastfiles')
df_out = pd.DataFrame(df)
df_out.to_csv('ticker_listCSE.csv', index=False)
blob2 = bucket2.blob('ticker_listCSE.csv')
blob2.upload_from_filename('ticker_listCSE.csv')

import pandas as pd
import requests
from pandas.compat import StringIO
import StringIO
import datetime
import ast
import json
import urllib
import itertools
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO as stio
else:
    from io import StringIO as stio

datevar=str(pd.to_datetime('today'))

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

#for canadian stocks http://financials.morningstar.com/ajax/exportKR2CSV.html?t=GOLD&region=CAN&culture=en-CA
link="http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB"
f = urllib.urlopen(link)

#Get the Financials
financials = pd.read_csv(f, sep=",",names=['measure','2007-12','2008-12','2009-12','2010-12','2011-12','2012-12','2013-12','2014-12','2015-12','2016-12','TTM'], skiprows=3, nrows=15)
link="http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB"
f = urllib.urlopen(link)
balance_sheet = pd.read_csv(f, sep=",",names=['measure','2007-12','2008-12','2009-12','2010-12','2011-12','2012-12','2013-12','2014-12','2015-12','2016-12','TTM'], skiprows=74, nrows=20)




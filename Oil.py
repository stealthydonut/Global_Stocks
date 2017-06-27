import urllib
import pandas as pd
import StringIO
import datetime
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO as stio
else:
    from io import StringIO as stio
    
ticker = ['APC','BTE','CVE','CLR','CRZO','DVN','GTE','HK','MRO','RRC','WLL']    
    
myfile = ''
for i in ticker:
    try:#Develop the text string that can get all the data
        start="http://finance.yahoo.com/d/quotes.csv?s="
        #date,Float Shares,Day's Low,Day's High,Open,Previous Close,Change,Volume,Name,Ticker,52 Low, 52 High,Dividend Share
        #end="&f=d1f6ghopc1vns"
        #date,Float ,Name,Ticker
        end="&f=d1f6s7oc1pghnsjkdk5j6r"
        str1 = ''.join([i])
        text2=start+str1+end    
        #Get the data from the yahoo api
        link=text2
        f = urllib.urlopen(link)
        myfile += f.readline()
    except:
        print i
     

    
TESTDATA=stio(myfile)

daily_prices = pd.read_csv(TESTDATA, sep=",", names=['date','Float Shares','Short Ratio','Open','Change','Previous Close','Low','High','Name','Ticker','52 Low','52 High','Dividend','Per change 52 H','Per change 52 L','PE Ratio'])
daily_prices['Div Yield']=(daily_prices['Dividend']/daily_prices['Previous Close'])*100


    

#The objective of this script is to identify the tickers on the major exchanges
#These datasets will be used for data extraction purposes

import urllib
import pandas as pd
#sudo -H pip install six==1.10.0
#sudo -H pip install html5lib==1.0b8
#sudo pip install beautifulsoup4
import html5lib
import beautifulsoup4

dls = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
urllib.urlretrieve(dls, "test.xls")
data = pd.read_csv('test.xls')

dls = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
urllib.urlretrieve(dls, "test.xls")
data = pd.read_csv('test.xls')

dls = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"
urllib.urlretrieve(dls, "test.xls")
data = pd.read_csv('test.xls')

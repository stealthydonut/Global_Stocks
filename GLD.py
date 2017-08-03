import pandas as pd
import requests
from pandas.compat import StringIO
dls = "http://www.spdrgoldshares.com/assets/dynamic/GLD/GLD_US_archive_EN.csv"
 
r = requests.get(dls)
daily_prices = pd.read_csv(StringIO(r.text), skiprows=6)

daily_prices2=daily_prices
daily_prices2['GLDdate']=pd.to_datetime(daily_prices2['Date'], errors='coerce')
daily_prices2['GLD Closex'] = daily_prices2.loc[daily_prices2[' GLD Close'].index, ' GLD Close'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['GLD Close']=pd.to_numeric(daily_prices2['GLD Closex'], errors='coerce')
daily_prices2['LBMA Gold Pricex'] = daily_prices2.loc[daily_prices2[' LBMA Gold Price'].index, ' LBMA Gold Price'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['LBMA Gold Pricex'] = daily_prices2.loc[daily_prices2['LBMA Gold Pricex'].index, 'LBMA Gold Pricex'].map(lambda x: str(x).replace('$',''))

daily_prices2['LBMA Gold Price']=pd.to_numeric(daily_prices2['LBMA Gold Pricex'], errors='coerce')
daily_prices2['NAV per GLD in Goldx'] = daily_prices2.loc[daily_prices2[' NAV per GLD in Gold'].index, ' NAV per GLD in Gold'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['NAV per GLD in Gold']=pd.to_numeric(daily_prices2['NAV per GLD in Goldx'], errors='coerce')
daily_prices2['NAV/sharex'] = daily_prices2.loc[daily_prices2[' NAV/share at 10.30 a.m. NYT'].index, ' NAV/share at 10.30 a.m. NYT'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['NAV/share']=pd.to_numeric(daily_prices2['NAV/sharex'], errors='coerce')
daily_prices2['Indicative Price of GLDx'] = daily_prices2.loc[daily_prices2[' Indicative Price of GLD at 4.15 p.m. NYT'].index, ' Indicative Price of GLD at 4.15 p.m. NYT'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['Indicative Price of GLD']=pd.to_numeric(daily_prices2['Indicative Price of GLDx'], errors='coerce')
daily_prices2['Mid point of bid/ask spreadx'] = daily_prices2.loc[daily_prices2[' Mid point of bid/ask spread at 4.15 p.m. NYT#'].index, ' Mid point of bid/ask spread at 4.15 p.m. NYT#'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['Mid point of bid/ask spreadx'] = daily_prices2.loc[daily_prices2['Mid point of bid/ask spreadx'].index, 'Mid point of bid/ask spreadx'].map(lambda x: str(x).replace('$',''))
daily_prices2['Mid point of bid/ask spread']=pd.to_numeric(daily_prices2['Mid point of bid/ask spreadx'], errors='coerce')
daily_prices2['Premium/Discount of GLD mid point v Indicative Value of GLDx'] = daily_prices2.loc[daily_prices2[' Premium/Discount of GLD mid point v Indicative Value of GLD at 4.15 p.m. NYT'].index, ' Premium/Discount of GLD mid point v Indicative Value of GLD at 4.15 p.m. NYT'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['Premium/Discount of GLD mid point v Indicative Value of GLDx'] = daily_prices2.loc[daily_prices2['Premium/Discount of GLD mid point v Indicative Value of GLDx'].index, 'Premium/Discount of GLD mid point v Indicative Value of GLDx'].map(lambda x: str(x).replace('%',''))
daily_prices2['Premium/Discount of GLD mid point v Indicative Value of GLD']=pd.to_numeric(daily_prices2['Premium/Discount of GLD mid point v Indicative Value of GLDx'], errors='coerce')
daily_prices2['Daily Share Volumex'] = daily_prices2.loc[daily_prices2[' Daily Share Volume'].index, ' Daily Share Volume'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['Daily Share Volume']=pd.to_numeric(daily_prices2['Daily Share Volumex'], errors='coerce')
daily_prices2['Total Net Asset Value Ounces in the Trustx'] = daily_prices2.loc[daily_prices2[' Total Net Asset Value Ounces in the Trust as at 4.15 p.m. NYT'].index, ' Total Net Asset Value Ounces in the Trust as at 4.15 p.m. NYT'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['Total Net Asset Value Ounces in the Trust']=pd.to_numeric(daily_prices2['Total Net Asset Value Ounces in the Trustx'], errors='coerce')
daily_prices2['Total Net Asset Value Tonnes in the Trustx'] = daily_prices2.loc[daily_prices2[' Total Net Asset Value Tonnes in the Trust as at 4.15 p.m. NYT'].index, ' Total Net Asset Value Tonnes in the Trust as at 4.15 p.m. NYT'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['Total Net Asset Value Tonnes in the Trust']=pd.to_numeric(daily_prices2['Total Net Asset Value Tonnes in the Trustx'], errors='coerce')
daily_prices2['Total Net Asset Value in the Trustx'] = daily_prices2.loc[daily_prices2[' Total Net Asset Value in the Trust'].index, ' Total Net Asset Value in the Trust'].map(lambda x: str(x).replace('HOLIDAY',''))
daily_prices2['Total Net Asset Value in the Trust']=pd.to_numeric(daily_prices2['Total Net Asset Value in the Trustx'], errors='coerce')

df = daily_prices2[['GLDdate','GLD Close','LBMA Gold Price','NAV per GLD in Gold','NAV/share','Indicative Price of GLD','Mid point of bid/ask spread',\
'Premium/Discount of GLD mid point v Indicative Value of GLD','Daily Share Volume','Total Net Asset Value Ounces in the Trust','Total Net Asset Value Tonnes in the Trust',\
'Total Net Asset Value in the Trust']]
df['cnt']=1

myfile = ''
start="http://finance.yahoo.com/d/quotes.csv?s="
end="&f=d1f6s7oc1pghnsjkdk5j6rv"
str1 = 'GLD'
text2=start+str1+end    
#Get the data from the yahoo api
link=text2
f = urllib.urlopen(link)
myfile += f.readline()
TESTDATA=stio(myfile)
daily_prices = pd.read_csv(TESTDATA, sep=",", names=['date','Float Shares','Short Ratio','Open','Change','Previous Close','Low','High','Name','Ticker','52 Low','52 High','Dividend','Per change 52 H','Per change 52 L','PE Ratio','Volume'])

print daily_prices


test['monthyear'] = test['GLDdate'].dt.strftime("%Y%m") 
test['shares outstanding']=267700000
dfile= test.groupby(['monthyear'], as_index=False)['cnt','GLDTotal Net Asset Value Ounced in Trust','shares outstanding'].sum()
dfile['ounces']=dfile['GLDTotal Net Asset Value Tonnes in Trust']/dfile['cnt']
dfile['claims per ounce']=dfile['GLDTotal Net Asset Value Ounced in Trust']/dfile['shares outstanding']
dfile['claims per ounce2']=dfile['shares outstanding']/dfile['GLDTotal Net Asset Value Ounced in Trust']


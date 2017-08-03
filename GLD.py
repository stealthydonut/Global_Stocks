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

print daily_prices2
df = daily_prices2[['GLDdate','GLD Close','LBMA Gold Price','NAV per GLD in Gold','NAV/share','Indicative Price of GLD','Mid point of bid/ask spread',\
'Premium/Discount of GLD mid point v Indicative Value of GLD','Daily Share Volume','Total Net Asset Value Ounces in the Trust','Total Net Asset Value Tonnes in the Trust',\
'Total Net Asset Value in the Trust']]

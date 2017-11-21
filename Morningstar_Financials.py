
import pandas as pd
import urllib

#for canadian stocks http://financials.morningstar.com/ajax/exportKR2CSV.html?t=GOLD&region=CAN&culture=en-CA
link="http://financials.morningstar.com/ajax/exportKR2CSV.html?t=FB"
f = urllib.urlopen(link)

#Get the Financials
daily_prices = pd.read_csv(f, sep=",",names=['measure','2007-12','2008-12','2009-12','2010-12','2011-12','2012-12','2013-12','2014-12','2015-12','2016-12','TTM'], skiprows=3, nrows=15)
print daily_prices
'measure','2007-12','2008-12','2009-12','2010-12','2011-12','2012-12','2013-12','2014-12','2015-12','2016-12','TTM'

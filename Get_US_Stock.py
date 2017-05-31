import urllib
import pandas as pd
import html5lib

dls = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
urllib.urlretrieve(dls, "test.xls")
data = pd.read_html('test.xls')
f_states=   pd.read_html('http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download') 

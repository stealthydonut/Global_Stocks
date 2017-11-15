import urllib
import re
import json
import csv
import pandas as pd
import datetime
###########################################
#Extract minute by minute bloomberg prices#
###########################################

htmltext = urllib.urlopen(" http://www.bloomberg.com/markets/chart/data/1D/AAPL:US")           
data = json.load(htmltext)
datapoints = data["data_values"]
labels=['time','price']
df = pd.DataFrame(datapoints, columns=labels)
labels=['time','price']
df['UNIXTIME'] = pd.to_datetime(df['time'], unit='ms')
#identify max/min value/open/close
dfmax=df['price'].max()
dfmin=df['price'].min()
dfmaxtime=df['UNIXTIME'].max()
dfmintime=df['UNIXTIME'].min()

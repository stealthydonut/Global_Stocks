####################################################################################################
#This program builds develops measures which will be used to diagnose general market high's and lows
####################################################################################################
import pandas as pd
import numpy as np
import quandl as qd
import os
import time
import datetime as dt
import pandas.core.algorithms as algos
import StringIO
from google.cloud import storage
client = storage.Client()
bucket = client.get_bucket('stagingarea')
# Then do other things...
blob = bucket.get_blob('closing_prices_histUS.csv')
# Define the object
content = blob.download_as_string()
#Because the pandas dataframe can only read from buffers or files, we need to take the string and put it into a buffer
inMemoryFile = StringIO.StringIO()
inMemoryFile.write(content)
#When you buffer, the "cursor" is at the end, and when you read it, the starting position is at the end and it will not pick up anything
inMemoryFile.seek(0)
#Note - anytime you read from a buffer you need to seek so it starts at the beginning
#The low memory false exists because there was a lot of data
bigdata=pd.read_csv(inMemoryFile, low_memory=False)
#############################################################################################################
#Generic Measures include: High, Low, Advance, Decline, cut by industry, etc, market cap changing on the bigs
#############################################################################################################

#Supply Side Measures

#Days to liquidate
#On balance volume


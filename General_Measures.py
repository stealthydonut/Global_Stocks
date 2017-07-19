import quandl
import urllib
import pandas as pd
import numpy as np
import StringIO
import datetime
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO as stio
else:
    from io import StringIO as stio
#import matplotlib
#import matplotlib.pyplot as plt
quandl.ApiConfig.api_key = 'BVno6pBYgcEvZJ6uctTr'
####################
#Get the Quandl Data
###################
ism = quandl.get("ISM/NONMAN_INVSENT")
gold = quandl.get("LBMA/GOLD")
silver = quandl.get("LBMA/SILVER")
oil = quandl.get("OPEC/ORB")
uranium = quandl.get("ODA/PURAN_USD")
ustax = quandl.get("FMSTREAS/MTS")
shiller = quandl.get("MULTPL/SHILLER_PE_RATIO_MONTH")
paladium = quandl.get("LPPM/PALL")
platinum = quandl.get("LPPM/PLAT")
balticdryindex = quandl.get("LLOYDS/BDI")
balticcapesizeindex = quandl.get("LLOYDS/BCI") #>150k DWT
balticsupramexindex = quandl.get("LLOYDS/BSI") #50-60k DWT
balticpanamaxindex = quandl.get("LLOYDS/BPI") #65-80k DWT
trade_Weigted_Index = quandl.get("FRED/TWEXBPA")
fed_funds_rate = quandl.get("FED/RIFSPFF_N_M")
fxusdcad = quandl.get("FRED/DEXCAUS")
fxusdyuan = quandl.get("FRED/DEXCHUS")
#US Reserves
res_ru = quandl.get("BANKRUSSIA/RESRV")
res_ca = quandl.get("FRED/TRESEGCAM052N")
#Gold Stock
gld_us = quandl.get("FRED/M1476CUSM144NNBR")

#libor3mth

######################
#Clean up Column Names
######################
gold.columns=['Gold USD (AM)','Gold USD (PM)','Gold GBP (AM)','Gold GBP (PM)','Gold EURO (AM)','Gold EURO (PM)']
silver.columns=['Silver USD','Silver GBP','Silver EURO']
oil.columns=['Oil USD']
shiller.columns=['Shiller Value']
ustax.columns=['US Receipts','US Outlays','US Deficit/Surplus (-)','US Borrowing from the Public','USReduction of Operating Cash','US By Other Means']
ism.columns=['ISM % Too High','ISM % About Right','ISM % Too Low','ISM Diffusion Index']
uranium.columns=['Uranium Value']
platinum.columns=['Platinum USD (AM)','Platinum USD (PM)','Platinum GBP (AM)','Platinum GBP (PM)','Platinum EURO (AM)','Platinum EURO (PM)']
paladium.columns=['Paladium USD (AM)','Paladium USD (PM)','Paladium GBP (AM)','Paladium GBP (PM)','Paladium EURO (AM)','Paladium EURO (PM)']
balticdryindex.columns=['balticdryindex Index']
balticcapesizeindex.columns=['balticcapesizeindex Index']
balticsupramexindex.columns=['balticsupramexindex Index']
balticpanamaxindex.columns=['balticpanamaxindex Index']
fxusdcad.columns=['cad/usd']
fxusdyuan.columns=['yuan/usd']
#################
#Index Generation
#################
gold['ind']=gold.index
silver['ind']=silver.index
oil['ind']=oil.index
paladium['ind']=paladium.index
platinum['ind']=platinum.index  
fxusdcad['ind']=fxusdcad.index
fxusdyuan['ind']=fxusdyuan.index
###########################
#Merge daily files together
###########################
df=gold.merge(silver, on='ind', how='outer')
df1=df.merge(paladium, on='ind', how='outer')
df2=df1.merge(platinum, on='ind', how='outer')
df3=df2.merge(fxusdcad, on='ind', how='outer')
df4=df3.merge(fxusdyuan, on='ind', how='outer')
daily_file=df4.merge(oil, on='ind', how='outer')
#################################
#Merge the monthly files together
#################################
ism['ind'] = ism.index
ism['monthyear'] = ism['ind'].dt.strftime("%m,%y")
uranium['ind'] = uranium.index
uranium['monthyear'] = uranium['ind'].dt.strftime("%m,%y")
ustax['ind'] = ustax.index
ustax['monthyear'] = ustax['ind'].dt.strftime("%m,%y")
########################################
#Create the monthly files for daily data
########################################
gold['monthyear'] = gold['ind'].dt.strftime("%m,%y")
gold['Gold daycnt'] = 1
goldmth = gold.groupby(['monthyear'], as_index=False)['Gold USD (AM)','Gold USD (PM)','Gold GBP (AM)','Gold GBP (PM)','Gold EURO (AM)','Gold EURO (PM)','Gold daycnt'].sum()
silver['monthyear'] = silver['ind'].dt.strftime("%m,%y")
silver['Silver daycnt'] = 1
silvermth = silver.groupby(['monthyear'], as_index=False)['Silver USD','Silver GBP','Silver EURO','Silver daycnt'].sum()
oil['monthyear'] = oil['ind'].dt.strftime("%m,%y")
oil['Oil daycnt'] = 1
oilmth = oil.groupby(['monthyear'], as_index=False)['Oil USD','Oil daycnt'].sum()
################################
#Merge the monthly data together
################################
mf=ustax.merge(goldmth, on='monthyear', how='outer')
mf1=mf.merge(silvermth, on='monthyear', how='outer')
mf2=mf1.merge(oilmth, on='monthyear', how='outer')
mf3=mf2.merge(ism, on='monthyear', how='outer')
monthly_file=mf3.merge(uranium, on='monthyear', how='outer')
############################
#Build measures on the files
############################
monthly_file['ma6 US Receipts'] = monthly_file['US Receipts'].rolling(window=6).mean()
monthly_file['ma6 ISM Diffusion Index'] = monthly_file['ISM Diffusion Index'].rolling(window=6).mean()
daily_file['Gold Silver Ratio']=daily_file['Gold USD (PM)']/daily_file['Silver USD']
daily_file['Gold Oil Ratio']=daily_file['Gold USD (PM)']/daily_file['Oil USD']
daily_file['Silver Oil Ratio']=daily_file['Silver USD']/daily_file['Oil USD']
daily_file['Gold_CAD']=daily_file['Gold USD (PM)']*daily_file['cad/usd']
daily_file['Gold_YUAN']=daily_file['Gold USD (PM)']*daily_file['yuan/usd']
daily_file['Gold_Total']=daily_file['Gold_CAD']+daily_file['Gold_YUAN']

   
        
#Put the dataset back into storage
from google.cloud import storage
client = storage.Client()
bucket2 = client.get_bucket('stagingarea')
df_out = pd.DataFrame(daily_file)
df_out.to_csv('general_measures.csv', index=False)
blob2 = bucket2.blob('general_measures.csv')
blob2.upload_from_filename('general_measures.csv')

import quandl
import urllib
import pandas as pd
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
import requests
from pandas.compat import StringIO

#import matplotlib
#import matplotlib.pyplot as plt

#Sourced from the following site https://github.com/mortada/fredapi

#########
#GLD Data
#########

dls = "http://www.spdrgoldshares.com/assets/dynamic/GLD/GLD_US_archive_EN.csv"
r = requests.get(dls)
daily_prices = pd.read_csv(StringIO(r.text), skiprows=6)


##########
#FRED Data
##########
from fredapi import Fred
fred = Fred(api_key='4af3776273f66474d57345df390d74b6')
#djia = fred.get_series_all_releases('DJIA')
treas10 = fred.get_series_all_releases('DGS10') #10-Year Treasury Constant Maturity Rate 
libor3 = fred.get_series_all_releases('USD3MTD156N') #libor
fedassets = fred.get_series_all_releases('WALCL')# All Federal Reserve Banks: Total Assets (WALCL) #Federal reserve balance sheet
libor12 = fred.get_series_all_releases('USD12MD156N')# 12 month libor

############
#Quandl Data
#############
quandl.ApiConfig.api_key = 'BVno6pBYgcEvZJ6uctTr'
####################
#Get the Quandl Data
###################
ism = quandl.get("ISM/NONMAN_INVSENT")
ism2 = quandl.get("ISM/MAN_PMI") #another ISM
gold = quandl.get("LBMA/GOLD")
silver = quandl.get("LBMA/SILVER")
#copper = quandl.get ("LME/PR_CU")  #copper
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
fxusdjap = quandl.get("FRED/DEXJPUS")
fxusdind = quandl.get("FRED/DEXINUS")
fxusdbra = quandl.get("FRED/DEXBZUS")
fxusdsko = quandl.get("FRED/DEXKOUS")
fxusdaud = quandl.get("FRED/DEXUSAL")
fxusdmex = quandl.get("FRED/DEXMXUS")
fxusdche = quandl.get("FRED/DEXSZUS")
fxusdeur = quandl.get("FED/RXI_US_N_B_EU")



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
fxusdjap.columns=['jap/usd']
fxusdind.columns=['ind/usd']
fxusdbra.columns=['bra/usd']
fxusdsko.columns=['sko/usd']
fxusdaud.columns=['aud/usd']
fxusdmex.columns=['mex/usd']
fxusdche.columns=['che/usd']
fxusdeur.columns=['eur/usd']
#######################
#Clean up the FRED data
#######################
libor3['libor3mth']=pd.to_numeric(libor3['value'], errors='coerce')
libor3['ind']=pd.to_datetime(libor3['date'], errors='coerce')
libor12['libor12mth']=pd.to_numeric(libor12['value'], errors='coerce')
libor12['ind']=pd.to_datetime(libor12['date'], errors='coerce')
treas10['treas10mth']=pd.to_numeric(treas10['value'], errors='coerce')
treas10['ind']=pd.to_datetime(treas10['date'], errors='coerce')
fedassets['fedassets']=pd.to_numeric(fedassets['value'], errors='coerce')
fedassets['ind']=pd.to_datetime(fedassets['date'], errors='coerce')
libor3x=libor3[['libor3mth','ind']]
libor12x=libor12[['libor12mth','ind']]
treas10x=treas10[['treas10mth','ind']]
fedassetsx=fedassets[['fedassets','ind']]
######################
#Clean up the GLD data
######################
daily_prices2=daily_prices
daily_prices2['ind']=pd.to_datetime(daily_prices2['Date'], errors='coerce')
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
dfgld = daily_prices2[['ind','GLD Close','LBMA Gold Price','NAV per GLD in Gold','NAV/share','Indicative Price of GLD','Mid point of bid/ask spread',\
'Premium/Discount of GLD mid point v Indicative Value of GLD','Daily Share Volume','Total Net Asset Value Ounces in the Trust','Total Net Asset Value Tonnes in the Trust',\
'Total Net Asset Value in the Trust']]


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
fxusdjap['ind']=fxusdjap.index
fxusdind['ind']=fxusdind.index
fxusdbra['ind']=fxusdbra.index
fxusdsko['ind']=fxusdsko.index
fxusdaud['ind']=fxusdaud.index
fxusdmex['ind']=fxusdmex.index
fxusdche['ind']=fxusdche.index
fxusdeur['ind']=fxusdeur.index         
###########################
#Merge daily files together
###########################
df=gold.merge(silver, on='ind', how='outer')
df1=df.merge(paladium, on='ind', how='outer')
df2=df1.merge(platinum, on='ind', how='outer')
df3=df2.merge(fxusdcad, on='ind', how='outer')
df4=df3.merge(fxusdyuan, on='ind', how='outer')
df5=df4.merge(fxusdjap, on='ind', how='outer')
df6=df5.merge(fxusdind, on='ind', how='outer')
df7=df6.merge(fxusdbra, on='ind', how='outer')
df8=df7.merge(fxusdsko, on='ind', how='outer')
df9=df8.merge(fxusdaud, on='ind', how='outer')
df10=df9.merge(fxusdmex, on='ind', how='outer')
df11=df10.merge(fxusdche, on='ind', how='outer')
df12=df11.merge(fxusdeur, on='ind', how='outer')
df13=df12.merge(libor3x, on='ind', how='outer')
df14=df13.merge(libor12x, on='ind', how='outer')
df15=df14.merge(fedassets, on='ind', how='outer')
df16=df15.merge(treas10x, on='ind', how='outer')
df17=df16.merge(dfgld, on='ind', how='outer')
daily_file=df17.merge(oil, on='ind', how='outer')


#################################
#Merge the monthly files together
#################################
ism['ind'] = ism.index
ism['monthyear'] = ism['ind'].dt.strftime("%m,%y")
ism2['ind'] = ism2.index
ism2['monthyear'] = ism2['ind'].dt.strftime("%m,%y")
uranium['ind'] = uranium.index
uranium['monthyear'] = uranium['ind'].dt.strftime("%m,%y")
ustax['ind'] = ustax.index
ustax['monthyear'] = ustax['ind'].dt.strftime("%m,%y")
shiller['ind'] = shiller.index
shiller['monthyear'] = shiller['ind'].dt.strftime("%m,%y")
balticdryindex['ind'] = balticdryindex.index
balticdryindex['monthyear'] = balticdryindex['ind'].dt.strftime("%m,%y")
balticcapesizeindex['ind'] = balticcapesizeindex.index
balticcapesizeindex['monthyear'] = balticcapesizeindex['ind'].dt.strftime("%m,%y")
balticsupramexindex['ind'] = balticsupramexindex.index
balticsupramexindex['monthyear'] = balticsupramexindex['ind'].dt.strftime("%m,%y")
balticpanamaxindex['ind'] = balticpanamaxindex.index
balticpanamaxindex['monthyear'] = balticpanamaxindex['ind'].dt.strftime("%m,%y")
trade_Weigted_Index['ind'] = trade_Weigted_Index.index
trade_Weigted_Index['monthyear'] = trade_Weigted_Index['ind'].dt.strftime("%m,%y")
fed_funds_rate['ind'] = fed_funds_rate.index
fed_funds_rate['monthyear'] = fed_funds_rate['ind'].dt.strftime("%m,%y")
########################################
#Create the monthly files for daily data
########################################
daily_file['monthyear'] = daily_file['ind'].dt.strftime("%m,%y")

mf=ustax.merge(daily_file, on='monthyear', how='outer')
mf1=mf.merge(ism, on='monthyear', how='outer')
mf2=mf1.merge(shiller, on='monthyear', how='outer')
mf3=mf2.merge(balticdryindex, on='monthyear', how='outer')
mf4=mf3.merge(balticcapesizeindex, on='monthyear', how='outer')
mf5=mf4.merge(balticsupramexindex, on='monthyear', how='outer')
mf6=mf5.merge(balticpanamaxindex, on='monthyear', how='outer')
mf7=mf6.merge(trade_Weigted_Index, on='monthyear', how='outer')
mf8=mf7.merge(fed_funds_rate, on='monthyear', how='outer')
daily_monthly_file=mf8.merge(uranium, on='monthyear', how='outer')

#################################################
#Create daycnts so the averages can be calculated
#################################################
daily_file['Gold daycnt'] = np.where(daily_file['Gold USD (AM)']>0, 1, 0)
daily_file['Silver daycnt'] = np.where(daily_file['Silver USD']>0, 1, 0)
daily_file['Oil daycnt'] = np.where(daily_file['Oil USD']>0, 1, 0)
daily_file['daycnt'] = 1
dailymth = daily_file.groupby(['monthyear'], as_index=False)['daycnt','Gold daycnt','Silver daycnt','Oil daycnt',\
'Gold USD (AM)','Gold USD (PM)','Gold GBP (AM)','Gold GBP (PM)','Gold EURO (AM)','Gold EURO (PM)',\
'Silver USD','Silver GBP','Silver EURO','Oil USD'].sum()

################################
#Merge the monthly data together
################################
mf=ustax.merge(dailymth, on='monthyear', how='outer')
mf1=mf.merge(ism, on='monthyear', how='outer')
mf2=mf1.merge(shiller, on='monthyear', how='outer')
mf3=mf2.merge(balticdryindex, on='monthyear', how='outer')
mf4=mf3.merge(balticcapesizeindex, on='monthyear', how='outer')
mf5=mf4.merge(balticsupramexindex, on='monthyear', how='outer')
mf6=mf5.merge(balticpanamaxindex, on='monthyear', how='outer')
mf7=mf6.merge(trade_Weigted_Index, on='monthyear', how='outer')
mf8=mf7.merge(fed_funds_rate, on='monthyear', how='outer')
monthly_file=mf8.merge(uranium, on='monthyear', how='outer')
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
daily_file['Gold_JAP']=daily_file['Gold USD (PM)']*daily_file['jap/usd']
daily_file['Gold_IND']=daily_file['Gold USD (PM)']*daily_file['ind/usd']
daily_file['Gold_BRA']=daily_file['Gold USD (PM)']*daily_file['bra/usd']
daily_file['Gold_SKO']=daily_file['Gold USD (PM)']*daily_file['sko/usd']
daily_file['Gold_AUD']=daily_file['Gold USD (PM)']*daily_file['aud/usd']
daily_file['Gold_MEX']=daily_file['Gold USD (PM)']*daily_file['mex/usd']
daily_file['Gold_CHE']=daily_file['Gold USD (PM)']*daily_file['che/usd']
daily_file['Gold_EUR']=daily_file['Gold USD (PM)']*daily_file['eur/usd']
daily_file['Gold_Total']=daily_file['Gold_CAD']+daily_file['Gold_YUAN']+daily_file['Gold_JAP']+daily_file['Gold_IND']+daily_file['Gold_BRA']+daily_file['Gold_SKO']+daily_file['Gold_AUD']+daily_file['Gold_MEX']+daily_file['Gold_CHE']+daily_file['Gold_EUR']

#Develop the reserve file
res_ru['Country']='RU'
res_ru['ind']=res_ru.index
res_jp['Country']='JP'
res_jp['ind']=res_jp.index
res_ca['Country']='CA'
res_ca['ind']=res_ca.index
bigdata = res_ru.append(res_jp, ignore_index=True)


ism2.to_excel('C:\Python27\commodity_file.xls', index=False)   
daily_file.to_excel('C:\Users\davking\Documents\My Tableau Repository\Datasources\commodity_file.xls', index=False)     
monthly_file.to_excel('C:\Users\davking\Documents\My Tableau Repository\Datasources\monthly_file.xls', index=False)     
   


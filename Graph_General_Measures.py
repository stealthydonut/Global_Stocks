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





####################################
#Clean up monthly file to be plotted
####################################
monthly_file['year'] = monthly_file['ind'].dt.strftime("%Y")
monthly_file['month'] = monthly_file['ind'].dt.strftime("%m")
monthly_file['day'] = monthly_file['ind'].dt.strftime("%d")
daily_file['year'] = daily_file['ind'].dt.strftime("%Y")
daily_file['month'] = daily_file['ind'].dt.strftime("%m")
daily_file['day'] = daily_file['ind'].dt.strftime("%d")


#This is for plotting data on a graph
#makes a new dataframe copy so that it does not refer back to original
test3=pd.DataFrame(test2[test2['index1'].notnull()])



monthly_filex=pd.DataFrame(monthly_file[monthly_file['ind'].notnull()])
monthly_filex.apply(lambda col: col.drop_duplicates().reset_index(drop=True))
test4['dateplotx'] = [dt.datetime(year=int(d.year), month=int(d.month), day=int(d.day)) for d in monthly_filex['ind']]


#This Generates a date axis on a daily basis - for monthly exclude day, and make day=1 on dateplot line
dateplot = []
dateplot2 = []
graph1 = []
##############################
#Create the dateplot variables
##############################
for month,year,day in zip(daily_file['month'], daily_file['year'], daily_file['day']):
        dateplot.append(dt.datetime(year=int(year), month=int(month), day=int(day)))
daily_file['dateplotx'] = [dt.datetime(year=d.year, month=d.month, day=d.day) for d in daily_file['ind']]
        

#build date time frame for monthly
for month,year,day in zip(test4['month'], test4['year'], test4['day']):
        dateplot2.append(dt.datetime(year=int(year), month=int(month), day=int(day)))       
daily_file['dateplotx'] = [dt.datetime(year=d.year, month=d.month, day=d.day) for d in daily_file['ind']]




   

#This is to convert everything into an array and to check the frequency
s1 = [float(x) for x in daily_file['Gold Silver Ratio']]
s2 = [float(x) for x in daily_file['Gold Oil Ratio']]
#s3 = [float(x) for x in test4['ma6tax']]
#s4 = [float(x) for x in test4['ma6spval']]
#s5 = [float(x) for x in afile['Ind_Close']]
#s6 = [float(x) for x in afile['ma10_150_delta']]
#s7 = [float(x) for x in afile['ma10_40_delta']]
#s8 = [float(x) for x in afile['ma10_ad10']]
s1=np.array(s1)
s2=np.array(s2)
#s3=np.array(s3)
#s4=np.array(s4)
#s5=np.array(s5)
#s6=np.array(s6)
#s7=np.array(s7)
#s8=np.array(s8)
dateplot=np.array(dateplot)
print('s1 - ' + str(len(s1)))
print('s2 - ' + str(len(s2)))
#print('s3 - ' + str(len(s3)))
#print('s4 - ' + str(len(s4)))
#print('s5 - ' + str(len(s5)))
#print('s6 - ' + str(len(s6)))
#print('s7 - ' + str(len(s7)))
#print('s8 - ' + str(len(s8)))
print('dateplot - ' + str(len(dateplot)))
#print('dateplot2 - ' + str(len(dateplot2)))

fig = plt.figure(figsize=(20,15))
#As soon as graph1 is initialized, everything below the block is included until another graph is initialized
graph1 = fig.add_subplot(411)
graph1.tick_params('y', colors='b')
graph1.plot(dateplot,s1,'b:', linewidth=2.0, label='G/S Ratio')
graph1.plot.grid(True)
graph1.legend(loc='upper left')

fig = plt.figure(figsize=(20,15))
graph2 = fig.add_subplot(411)
graph2.tick_params('y', colors='b')
graph2.plot(dateplot,s2,'r:', linewidth=2.0, label='G/O Ratio')
graph2.plot.grid(True)
graph2.legend(loc='upper left')
plt.show

fig = plt.figure(figsize=(20,15))
#sA soon as graph1 is initialized, everything below the block is included until another graph is initialized
graph1 = fig.add_subplot(411)
graph1.tick_params('y', colors='b')
graph1.plot(dateplot,s1,'b:', linewidth=2.0, label='G/S Ratio')
graph1.plot(dateplot,s2,'k:', linewidth=2.0, dashes=(10,10), label='G/O Ratio')

start, end = graph1.get_xlim()
#Ticks on the axis
graph1.xaxis.set_ticks(np.arange(start, end, 3.0 *365))
graph1.plot()
graph1.legend(loc='upper left')

#Build the graph on two axes


fig = plt.figure(figsize=(20,15))
#As soon as graph1 is initialized, everything below the block is included until another graph is initialized
graph1 = fig.add_subplot(411)
graph1.tick_params('y', colors='b')
graph1.plot(dateplot,s1,'b:', linewidth=2.0, label='G/S Ratio')
#graph1.plot(dateplot,s2,'k:', linewidth=2.0, dashes=(5,10), label='150dayL')
start, end = graph1.get_xlim()
graph2 = graph1.twinx() #this creates the same x axis with an independent y
graph2.tick_params('y', colors='r')
#graph2.plot(dateplot,s2,'r-', linewidth=2.0, label='G/O Ratio')
graph2.plot(dateplot,s2,'r-', linewidth=1.0)
graph2.plot(dateplot,s2,'r:', linewidth=2.0, label='G/O Ratio')
graph2.xaxis.set_ticks(np.arange(start, end, 4.0 *365))
plt.show


fig = plt.figure(figsize=(20,15))
#As soon as graph1 is initialized, everything below the block is included until another graph is initialized
graph1 = fig.add_subplot(411)
graph1.tick_params('y', colors='b')
graph1.plot(dateplot2,s3,'b:', linewidth=2.0, label='G/S Ratio')
graph1.set_ylabel('US Tax Receipts')
plt.legend(loc='best')
#graph1.plot(dateplot,s2,'k:', linewidth=2.0, dashes=(5,10), label='150dayL')
start, end = graph1.get_xlim()
graph2 = graph1.twinx() #this creates the same x axis with an independent y
graph2.tick_params('y', colors='r')
graph2.set_ylabel('S&P500')
#graph2.plot(dateplot,s2,'r-', linewidth=2.0, label='G/O Ratio')
graph2.plot(dateplot2,s4,'r-', linewidth=1.0)
graph2.plot(dateplot2,s4,'r:', linewidth=2.0, label='G/O Ratio')
plt.legend(loc='best')
graph2.xaxis.set_ticks(np.arange(start, end, 4.0 *365))
plt.show


        
        
#This is to convert everything into an array and to check the frequency
s1 = [float(x) for x in pfile['gs_ratio']]
s2 = [float(x) for x in pfile['go_ratio']]
#s3 = [float(x) for x in afile['ma10_h40']]
#s4 = [float(x) for x in afile['ma10_l40']]
#s5 = [float(x) for x in afile['Ind_Close']]
#s6 = [float(x) for x in afile['ma10_150_delta']]
#s7 = [float(x) for x in afile['ma10_40_delta']]
#s8 = [float(x) for x in afile['ma10_ad10']]
s1=np.array(s1)
s2=np.array(s2)
#s3=np.array(s3)
#s4=np.array(s4)
#s5=np.array(s5)
#s6=np.array(s6)
#s7=np.array(s7)
#s8=np.array(s8)
dateplot=np.array(dateplot)
print('s1 - ' + str(len(s1)))
print('s2 - ' + str(len(s2)))
#print('s3 - ' + str(len(s3)))
#print('s4 - ' + str(len(s4)))
#print('s5 - ' + str(len(s5)))
#print('s6 - ' + str(len(s6)))
#print('s7 - ' + str(len(s7)))
#print('s8 - ' + str(len(s8)))
print('dateplot - ' + str(len(dateplot)))

fig = plt.figure(figsize=(20,15))
#As soon as graph1 is initialized, everything below the block is included until another graph is initialized
graph1 = fig.add_subplot(411)
graph1.tick_params('y', colors='b')
graph1.plot(dateplot,s1,'b:', linewidth=2.0, label='G/S Ratio')
#graph1.plot(dateplot,s2,'k:', linewidth=2.0, dashes=(5,10), label='150dayL')
graph1.legend(loc='upper left')
graph1.set_ylabel('High and Lows Over 150 Days')
graph1.axes.xaxis.set_ticklabels([])
graph2 = graph1.twinx() #this creates the same x axis with an independent y
graph2.tick_params('y', colors='r')
graph2.set_ylabel('Index Close')
graph2.plot(dateplot,s2,'r-', linewidth=1.0)
plt.show

graph3 = fig.add_subplot(412)
graph3.tick_params('y', colors='b')
graph3.plot(dateplot,s2,'b:', linewidth=3.0, label='40dayH')
#graph3.plot(dateplot,s4,'k:', linewidth=3.0, dashes=(5,10), label='40dayL')
graph3.legend(loc='upper left')
graph3.set_ylabel('High and Lows Over 40 Days')
graph3.axes.xaxis.set_ticklabels([])
graph4 = graph3.twinx() #this creates the same x axis with an independent y
graph4.tick_params('y', colors='r')
graph4.set_ylabel('Index Close')
graph4.plot(dateplot,s5,'r-', linewidth=0.5)
plt.show

graph5 = fig.add_subplot(413)
graph5.tick_params('y', colors='b')
graph5.plot(dateplot,s6,'g:', linewidth=2.0, label='Delta for MA150')
graph5.plot(dateplot,s7,'c:', linewidth=2.0, label='Delta for MA40')
graph5.legend(loc='upper left')
graph5.set_ylabel('High and Lows Over 40 Days')
graph6 = graph5.twinx() #this creates the same x axis with an independent y
graph6.tick_params('y', colors='r')
graph6.set_ylabel('Index Close')
graph6.plot(dateplot,s5,'r-', linewidth=0.5)
plt.show

graph7 = fig.add_subplot(414)
graph7.tick_params('y', colors='b')
graph7.plot(dateplot,s8,'g:', linewidth=2.0, label='10 Day Advance Decline')
graph7.legend(loc='upper left')
graph7.set_ylabel('High and Lows Over 40 Days')
graph8 = graph7.twinx() #this creates the same x axis with an independent y
graph8.tick_params('y', colors='r')
graph8.set_ylabel('Index Close')
graph8.plot(dateplot,s5,'r-', linewidth=0.5)
plt.show

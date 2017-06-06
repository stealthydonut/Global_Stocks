import quandl
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
quandl.ApiConfig.api_key = 'BVno6pBYgcEvZJ6uctTr'
ism = quandl.get("ISM/NONMAN_INVSENT")
gold = quandl.get("LBMA/GOLD")
silver = quandl.get("LBMA/SILVER")
oil = quandl.get("OPEC/ORB")

#Index Generation
gold['ind']=gold.index
silver['ind']=silver.index
oil['ind']=oil.index
pfile=gold.merge(silver, on='ind', how='outer')

pfile['gs_ratio']=pfile['USD (PM)']/pfile['USD']


#data manipulation to get a month and year variaable
#ism['index1'] = ism.index
#ism['monthyear'] = ism['index1'].dt.strftime("%m,%y")
#gold['index1'] = gold.index
#gold['monthyear'] = gold['index1'].dt.strftime("%m,%y")
#test=gold.merge(ism_gold, on='monthyear', how='outer')


pfile['dateplotx'] = [dt.datetime(year=d.year, month=d.month, day=d.day) for d in pfile['ind']]


pfile['year'] = pfile['ind'].dt.strftime("%Y")
pfile['month'] = pfile['ind'].dt.strftime("%m")
pfile['day'] = pfile['ind'].dt.strftime("%d")
#This Generates a date axis on a daily basis - for monthly exclude day, and make day=1 on dateplot line
dateplot = []
graph1 = []
for month,year,day in zip(pfile['month'], pfile['year'], pfile['day']):
        dateplot.append(dt.datetime(year=int(year), month=int(month), day=int(day)))
        
        
#This is to convert everything into an array and to check the frequency
s1 = [float(x) for x in pfile['gs_ratio']]
#s2 = [float(x) for x in afile['ma10_l150']]
#s3 = [float(x) for x in afile['ma10_h40']]
#s4 = [float(x) for x in afile['ma10_l40']]
#s5 = [float(x) for x in afile['Ind_Close']]
#s6 = [float(x) for x in afile['ma10_150_delta']]
#s7 = [float(x) for x in afile['ma10_40_delta']]
#s8 = [float(x) for x in afile['ma10_ad10']]
s1=np.array(s1)
#s2=np.array(s2)
#s3=np.array(s3)
#s4=np.array(s4)
#s5=np.array(s5)
#s6=np.array(s6)
#s7=np.array(s7)
#s8=np.array(s8)
dateplot=np.array(dateplot)
print('s1 - ' + str(len(s1)))
#print('s2 - ' + str(len(s2)))
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
graph1.plot.grid(True)
graph1.legend(loc='upper left')
        
        
#This is to convert everything into an array and to check the frequency
s1 = [float(x) for x in pfile['gs_ratio']]
#s2 = [float(x) for x in afile['ma10_l150']]
#s3 = [float(x) for x in afile['ma10_h40']]
#s4 = [float(x) for x in afile['ma10_l40']]
#s5 = [float(x) for x in afile['Ind_Close']]
#s6 = [float(x) for x in afile['ma10_150_delta']]
#s7 = [float(x) for x in afile['ma10_40_delta']]
#s8 = [float(x) for x in afile['ma10_ad10']]
s1=np.array(s1)
#s2=np.array(s2)
#s3=np.array(s3)
#s4=np.array(s4)
#s5=np.array(s5)
#s6=np.array(s6)
#s7=np.array(s7)
#s8=np.array(s8)
dateplot=np.array(dateplot)
print('s1 - ' + str(len(s1)))
#print('s2 - ' + str(len(s2)))
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
graph2.plot(dateplot,s5,'r-', linewidth=1.0)
plt.show

graph3 = fig.add_subplot(412)
graph3.tick_params('y', colors='b')
graph3.plot(dateplot,s3,'b:', linewidth=3.0, label='40dayH')
graph3.plot(dateplot,s4,'k:', linewidth=3.0, dashes=(5,10), label='40dayL')
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


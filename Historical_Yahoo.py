
#Get todays date
year = datetime.date.today().year
day = datetime.date.today().day
#Month
month = datetime.datetime.now()
month2=month.strftime('%B')
myfile = ''
bigdata = pd.DataFrame()

for i in df2:
    try:#Develop the text string that can get all the data
        stringone='https://query1.finance.yahoo.com/v7/finance/download/'
        stringtwo='?period=1493819016&period2=1496497416&interval=1d&events=history&crumb=RkgV3tFpvN8'
        ticker=''.join([i])
        text2=stringone+ticker+stringtwo      
        data = pd.read_csv(text2)
        data['ticker']= i
        bigdata = bigdata.append(data, ignore_index=False)
    except:
        print i




Jan 12 - Jun 2

https://query1.finance.yahoo.com/v7/finance/download/RES.TO?period=893819016&period2=1496497412&interval=1d&events=history&crumb=RkgV3tFpvN8

import pandas as pd

df = pd.read_csv('C:\Users\davking\Desktop\SOUTH_AFRICA_CUSTOMS_FLOWS_Raw.csv')
#df['CountryOfDestinationName'] = df['CountryOfDestinationName'].astype(str)
df['CountryOfDestinationName2'] = df['CountryOfDestinationName'].astype(str)
df['CountryOfDestinationName2'] = df['CountryOfDestinationName'].str.split(',') 
df_metal=df['StatisticalUnit']=='KG'
df_metal2=df_metal['TariffAndDescription']=='71101900'
      
           
           
dailymth = df_metal.groupby(['cntry'], as_index=False)['CustomsValue'].sum()         

print df.dtypes

df['tot_value']=df['CustomsValue']/df['StatisticalQuantity']


df['TariffAndDescription']='71101900'

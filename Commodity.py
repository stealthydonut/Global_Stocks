#Crude Oil OPEC/ORB
#Gold Price LBMA/GOLD
#Silver Price LBMA/SILVER


import quandl
import pandas as pd
quandl.ApiConfig.api_key = 'BVno6pBYgcEvZJ6uctTr'
ism = quandl.get("ISM/NONMAN_INVSENT")
gold = quandl.get("LBMA/GOLD")
silver = quandl.get("LBMA/SILVER")
oil = quandl.get("OPEC/ORB")

#Index Generation
gold['ind']=gold.index
silver['ind']=silver.index
oil['ind']=oil.index
test=gold.merge(silver, on='ind', how='outer')


#data manipulation to get a month and year variaable
ism['index1'] = ism.index
ism['monthyear'] = ism['index1'].dt.strftime("%m,%y")
gold['index1'] = gold.index
gold['monthyear'] = gold['index1'].dt.strftime("%m,%y")

test=gold.merge(ism_gold, on='monthyear', how='outer')

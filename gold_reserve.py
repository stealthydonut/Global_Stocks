#This script takes data from the world gold council and with simple transformation calculates the

import pandas as pd
import numpy as np
gold_df = pd.read_csv("C:/Users/davking/Desktop/Python/gold.csv")
res_df = pd.read_csv("C:/Users/davking/Desktop/Python/res.csv")

#del bopdata
#del reserve
#del bigdata
####################################################
#Generates the Gold and FX Reserves for Each Country
####################################################
colist=[['Q1 2000','3/31/2000'],['Q2 2000','6/30/2000'],['Q3 2000','9/29/2000'],['Q4 2000','12/29/2000'],['Q1 2001','3/30/2001'],['Q2 2001','6/29/2001'],\
['Q3 2001','9/28/2001'],['Q4 2001','12/31/2001'],['Q1 2002','3/29/2002'],['Q2 2002','6/28/2002'],['Q3 2002','9/30/2002'],['Q4 2002','12/31/2002'],\
['Q1 2003','3/29/2003'],['Q2 2003','6/28/2003'],['Q3 2003','9/28/2003'],['Q4 2003','12/31/2003'],['Q1 2004','3/29/2004'],['Q2 2004','6/28/2004'],['Q3 2004','9/28/2004'],\
['Q4 2004','12/31/2004'],['Q1 2005','3/29/2005'],['Q2 2005','6/28/2005'],['Q3 2005','9/28/2005'],['Q4 2005','12/31/2005'],['Q1 2006','3/29/2006'],\
['Q2 2006','6/28/2006'],['Q3 2006','9/28/2006'],['Q4 2006','12/31/2006'],['Q1 2007','3/29/2007'],['Q2 2007','6/28/2007'],['Q3 2007','9/28/2007'],['Q4 2007','12/31/2007'],['Q1 2008','3/29/2008'],\
['Q2 2008','6/28/2008'],['Q3 2008','9/28/2008'],['Q4 2008','12/31/2008'],['Q1 2009','3/29/2009'],['Q2 2009','6/28/2009'],['Q3 2009','9/28/2009'],['Q4 2009','12/31/2009'],\
['Q1 2010','3/29/2010'],['Q2 2010','6/28/2010'],['Q3 2010','9/28/2010'],['Q4 2010','12/31/2010'],['Q1 2011','3/29/2011'],['Q2 2011','6/28/2011'],['Q3 2011','9/28/2011'],\
['Q4 2011','12/31/2011'],['Q1 2012','3/29/2012'],['Q2 2012','6/28/2012'],['Q3 2012','9/28/2012'],['Q4 2012','12/31/2012'],['Q1 2013','3/29/2013'],['Q2 2013','6/28/2013'],\
['Q3 2013','9/28/2013'],['Q4 2013','12/31/2013'],['Q1 2014','3/29/2014'],['Q2 2014','6/28/2014'],['Q3 2014','9/28/2014'],['Q4 2014','12/31/2014'],['Q1 2015','3/29/2015'],\
['Q2 2015','6/28/2015'],['Q3 2015','9/28/2015'],['Q4 2015','12/31/2015'],['Q1 2016','3/29/2016'],['Q2 2016','6/28/2016'],['Q3 2016','9/28/2016'],['Q4 2016','12/31/2016'],\
['Q1 2017','3/29/2017']]



bigdata = pd.DataFrame()
reserve = pd.DataFrame()

for i in colist:
    ticker=''.join(i[0])   
    df = gold_df[['Unnamed: 0',ticker]]
    df.columns=['countryx','gold amount']
    df['quarter']=''.join(i[0])
    df['date']=''.join(i[1])
    df['Gold Tonnex'] = df.loc[df['gold amount'].index, 'gold amount'].map(lambda x: x.replace('-','0'))
    df['Gold Tonne'] = df.loc[df['Gold Tonnex'].index, 'Gold Tonnex'].map(lambda x: str(x).replace(',',''))
    df['country2'] = df.loc[df['countryx'].index, 'countryx'].map(lambda x: x.replace(')',''))
    df['country']=df['country2'].str.upper()
    bigdata = bigdata.append(df, ignore_index=False)

for i in colist:
    ticker=''.join(i[0])   
    df = res_df[['Unnamed: 0',ticker]]
    df.columns=['countryx','fxamount']
    df['quarter']=''.join(i[0])
    df['date']=''.join(i[1])
    df['FX Reservex'] = df.loc[df['fxamount'].index, 'fxamount'].map(lambda x: x.replace('-','0'))
    df['FX Reserve'] = df.loc[df['FX Reservex'].index, 'FX Reservex'].map(lambda x: str(x).replace(',',''))
    df['country2'] = df.loc[df['countryx'].index, 'countryx'].map(lambda x: x.replace(')',''))
    df['country']=df['country2'].str.upper()
    reserve = reserve.append(df, ignore_index=False)

#del bopdata
#del reserve
#del bigdata

######################################
#Generates the U.S Balance of Payments
######################################

import quandl as qd
#Get the quandl API key
qd.ApiConfig.api_key = 'BVno6pBYgcEvZJ6uctTr'
#Use a list to generate a dataset
boplist =['Afghanistan','USCENSUS/IE_5310','AF'],['Albania','USCENSUS/IE_4810','AL'],['Algeria','USCENSUS/IE_7210','DZ'],['Andorra','USCENSUS/IE_4271','AD'],['Angola','USCENSUS/IE_7620','AO'],['Anguilla','USCENSUS/IE_2481','AI'],['Antigua and Barbuda','USCENSUS/IE_2484','AG'],['Argentina','USCENSUS/IE_3570','AR'],\
['Armenia','USCENSUS/IE_4631','AM'],['Aruba','USCENSUS/IE_2779','AW'],['Australia','USCENSUS/IE_6021','AU'],['Austria','USCENSUS/IE_4330','AT'],['Azerbaijan','USCENSUS/IE_4632','AZ'],['Bahamas','USCENSUS/IE_2360','BS'],\
['Bahrain','USCENSUS/IE_5250','BH'],['Bangladesh','USCENSUS/IE_5380','BD'],['Barbados','USCENSUS/IE_2720','BB'],['Belarus','USCENSUS/IE_4622','BY'],['Belgium','USCENSUS/IE_4231','BE'],\
['Belize','USCENSUS/IE_2080','BZ'],['Benin','USCENSUS/IE_7610','BJ'],['Bhutan','USCENSUS/IE_5682','BT'],['Bolivia','USCENSUS/IE_3350','BO'],['Bosnia','USCENSUS/IE_4793','BA'],['Botswana','USCENSUS/IE_7930','BW'],['Brazil','USCENSUS/IE_3510','BR'],['British Virgin Islands','USCENSUS/IE_2482','VG'],\
['Bulgaria','USCENSUS/IE_4870','BG'],['Burkina Faso','USCENSUS/IE_7600','BF'],['Burma','USCENSUS/IE_5460','MM'],['Burundi','USCENSUS/IE_7670','BI'],['Cambodia','USCENSUS/IE_5550','KH'],['Cameroon','USCENSUS/IE_7420','CM'],['Canada','USCENSUS/IE_1220','CA'],\
['Cape Verde','USCENSUS/IE_7643','CV'],['Cayman Islands','USCENSUS/IE_2440','CY'],['Central African Republic','USCENSUS/IE_7540','CF'],['Chad','USCENSUS/IE_7560','TD'],['Chile','USCENSUS/IE_3370','CL'],['China','USCENSUS/IE_5700','CN'],['Colombia','USCENSUS/IE_3010','CO'],['Comoros','USCENSUS/IE_7890','KM'],\
['Congo','USCENSUS/IE_7630','CD'],['Costa Rica','USCENSUS/IE_2230','CR'],['Cote dIvoire','USCENSUS/IE_7480','CI'],['Croatia','USCENSUS/IE_4791','HR'],['Cuba','USCENSUS/IE_2390','CU'],['Cyprus','USCENSUS/IE_4910','CY'],['Czech Republic','USCENSUS/IE_4351','CZ'],\
['Denmark','USCENSUS/IE_4099','DK'],['Dijbouti','USCENSUS/IE_7770','DJ'],['Dominca','USCENSUS/IE_2486','DM'],['Domincan Republic','USCENSUS/IE_2470','DO'],['Ecuador','USCENSUS/IE_3310','EC'],['Egypt','USCENSUS/IE_7290','EG'],['El Salvador','USCENSUS/IE_2110','ES'],['Equatorial','USCENSUS/IE_7380','Country'],\
['Eritrea','USCENSUS/IE_7741','ER'],['Estonia','USCENSUS/IE_4470','ES'],['Ethiopia','USCENSUS/IE_7749','ET'],['Fiji','USCENSUS/IE_6863','FJ'],['Finland','USCENSUS/IE_4050','FI'],['France','USCENSUS/IE_4279','FR'],['Gabon','USCENSUS/IE_7550','GA'],['Gambia','USCENSUS/IE_7500','GM'],['Georgia','USCENSUS/IE_4633','GE'],['Germany','USCENSUS/IE_4280','DE'],\
['Ghana','USCENSUS/IE_7490','GH'],['Greece','USCENSUS/IE_4840','GR'],['Grenada','USCENSUS/IE_2489','GD'],['Guatemala','USCENSUS/IE_2050','GT'],['Guinea  ','USCENSUS/IE_7460','GN'],['Guinea-Bissau','USCENSUS/IE_7642','GW'],['Guyana','USCENSUS/IE_3120','GY'],['Haiti','USCENSUS/IE_2450','HT'],['Honduras','USCENSUS/IE_2150','HN'],\
['Hong Kong','USCENSUS/IE_5820','HK'],['Hungary','USCENSUS/IE_4370','HU'],['Iceland','USCENSUS/IE_4000','IS'],['India','USCENSUS/IE_5330','IN'],['Indonesia','USCENSUS/IE_5600','ID'],['Iran','USCENSUS/IE_5070','IR'],['Iraq','USCENSUS/IE_5050','IQ'],\
['Ireland','USCENSUS/IE_4190','IE'],['Israel','USCENSUS/IE_5081','IL'],['Italy','USCENSUS/IE_4759','IT'],['Jamaica','USCENSUS/IE_2410','JM'],['Japan','USCENSUS/IE_5880','JP'],['Jordan','USCENSUS/IE_5110','JO'],['Kazakhastan','USCENSUS/IE_4634','KZ'],['Kenya','USCENSUS/IE_7790','KE'],['Kyrgyzstan','USCENSUS/IE_4635','KG'],['Laos','USCENSUS/IE_5530','LA'],\
['Latvia','USCENSUS/IE_4490','LV'],['Lebanon','USCENSUS/IE_5040','LB'],['Lechtenstein','USCENSUS/IE_4411','LI'],['Lesotho','USCENSUS/IE_7990','LS'],['Liberia','USCENSUS/IE_7650','LR'],['Libya','USCENSUS/IE_7250','LY'],['Lithuania','USCENSUS/IE_4510','LT'],['Luxembourg','USCENSUS/IE_4239','LU'],\
['Macedonia','USCENSUS/IE_4794','MK'],['Madagascar','USCENSUS/IE_7880','MG'],['Malawi','USCENSUS/IE_7970','MW'],['Malaysia','USCENSUS/IE_5570','MY'],['Maldives','USCENSUS/IE_5683','MV'],['Mali','USCENSUS/IE_7450','ML'],['Malta','USCENSUS/IE_4730','MT'],['Marshall Islands','USCENSUS/IE_6810','MH'],['Martinique','USCENSUS/IE_2839','MQ'],['Mauritania','USCENSUS/IE_7410','MR'],\
['Mauritius','USCENSUS/IE_7850','MU'],['Mexico','USCENSUS/IE_2010','MX'],['Micronesia','USCENSUS/IE_6820','FM'],['Moldova','USCENSUS/IE_4641','MD'],['Monaco','USCENSUS/IE_4272','MC'],['Mongolia','USCENSUS/IE_5740','MN'],\
['Montenegro','USCENSUS/IE_4804','ME'],['Morocco','USCENSUS/IE_7140','MA'],['Mozambique','USCENSUS/IE_7870','MZ'],['Namibia','USCENSUS/IE_7920','NA'],['Nauru','USCENSUS/IE_6862','NR'],['Nepal','USCENSUS/IE_5360','NP'],['Netherlands','USCENSUS/IE_4210','NL'],['New Zealand','USCENSUS/IE_6141','NZ'],['Nicaragua','USCENSUS/IE_2190','NI'],\
['Niger','USCENSUS/IE_7510','NE'],['Nigeria','USCENSUS/IE_7530','NG'],['North Korea','USCENSUS/IE_5790','KP'],['Norway','USCENSUS/IE_4039','NO'],['Oman','USCENSUS/IE_5230','OM'],['Pakistan','USCENSUS/IE_5350','PK'],['Palau','USCENSUS/IE_6830','PW'],['Panama','USCENSUS/IE_2250','PA'],['Papau New Guinea','USCENSUS/IE_6040','PG'],['Paraguay','USCENSUS/IE_3530','PY'],\
['Peru','USCENSUS/IE_3330','PE'],['Philippines','USCENSUS/IE_5650','PH'],['Poland','USCENSUS/IE_4550','PL'],['Portugal','USCENSUS/IE_4710','PT'],['Qatar','USCENSUS/IE_5180','QA'],['Romania','USCENSUS/IE_4850','RO'],['Russia','USCENSUS/IE_4621','RU'],\
['Rwanda','USCENSUS/IE_7690','RW'],['Saint Kitts','USCENSUS/IE_2483','KN'],['Saint Vincent','USCENSUS/IE_2488','VC'],['Samoa','USCENSUS/IE_6150','WS'],['San Tome','USCENSUS/IE_7644','Country'],\
['Saudi Arabia','USCENSUS/IE_5170','SA'],['Senegal','USCENSUS/IE_7440','SN'],['Serbia','USCENSUS/IE_4801','RS'],['Seychelles','USCENSUS/IE_7800','SC'],['Sierra Leone','USCENSUS/IE_7470','SL'],['Singapore','USCENSUS/IE_5590','SG'],\
['Slovakia','USCENSUS/IE_4359','SK'],['Slovenia','USCENSUS/IE_4792','SI'],['Solomon Islands','USCENSUS/IE_6223','SB'],['Somalia','USCENSUS/IE_7700','SO'],['South Africa','USCENSUS/IE_7910','ZA'],['South Korea','USCENSUS/IE_5800','KR'],\
['South Sudan','USCENSUS/IE_7323','SS'],['Spain','USCENSUS/IE_4700','ES'],['Sri Lanka','USCENSUS/IE_5420','LK'],['Sudan','USCENSUS/IE_7321','SD'],['Suriname','USCENSUS/IE_3150','SR'],\
['Swaziland','USCENSUS/IE_7950','SZ'],['Sweden','USCENSUS/IE_4010','SE'],['Switzerland','USCENSUS/IE_4419','CH'],['Syria','USCENSUS/IE_5020','SY'],['Taiwan','USCENSUS/IE_5830','TW'],['Tajikistan','USCENSUS/IE_4642','TJ'],\
['Tanzania','USCENSUS/IE_7830',''],['Thailand','USCENSUS/IE_5490','TH'],['Timor-Leste','USCENSUS/IE_5601','TL'],['Togo','USCENSUS/IE_7520','TG'],['Tonga','USCENSUS/IE_6864','TO'],['Trinidad','USCENSUS/IE_2740','TT'],\
['Tunisia','USCENSUS/IE_7230','TN'],['Turkey','USCENSUS/IE_4890','TR'],['Turkmenistan','USCENSUS/IE_4643','TM'],['Turks and Caicos','USCENSUS/IE_2430','TC'],['Tuvalu','USCENSUS/IE_6227','TV'],['Uganda','USCENSUS/IE_7780','UG'],\
['Ukraine','USCENSUS/IE_4623','UA'],['United Arab Emirates','USCENSUS/IE_5200','AE'],['United Kingdom','USCENSUS/IE_4120','GB'],['Uruguay','USCENSUS/IE_3550','UY'],['Uzbekistan','USCENSUS/IE_4644','UZ'],['Vanuatu','USCENSUS/IE_6224','VU'],\
['Vatican City','USCENSUS/IE_4752','VA'],['Venezuela','USCENSUS/IE_3070','VE'],['Vietnam','USCENSUS/IE_5520','VN'],['Yemen','USCENSUS/IE_5210','YE'],['Zambia','USCENSUS/IE_7940','ZM'],['Zimbabwe','USCENSUS/IE_7960','ZW'],\
['Kosovo','USCENSUS/IE_4803','XK'],['Kuwait','USCENSUS/IE_5130','KW']
 
bopdata = pd.DataFrame()
##################################### 
#Generate the balance of payment file
#####################################
for i in boplist:
    test=qd.get(i[1]).copy(deep=True)
    #Create a month/year variable   
    test['country'] = i[2]
    test['index1'] = test.index
    test['monthyear'] = test['index1'].dt.strftime("%y%m")  
    test['year'] = test['index1'].dt.strftime("%Y") 
    test['month'] = test['index1'].dt.strftime("%m")
    bopdata = bopdata.append(test, ignore_index=True)

#####################################
#Begin to break the files in quarters
#####################################
bopdata['monthnum']=pd.to_numeric(bopdata['month'], errors='coerce')
bopdata['fl1'] = np.where(bopdata['monthnum']<4, 'Q1', 'no')
bopdata['fl2'] = np.where((bopdata['monthnum']>3) & (bopdata['monthnum']<7), 'Q2', 'no')
bopdata['fl3'] = np.where((bopdata['monthnum']>6) & (bopdata['monthnum']<10), 'Q3', 'no')
bopdata['fl4'] = np.where(bopdata['monthnum']>9, 'Q4', 'no')
q1=bopdata[bopdata['fl1']=='Q1']
q1['merge']=q1['fl1']+" "+q1['year'].map(str)
#Select only columns required
q1gold=q1[['Exports','Imports','Balance','country','merge']]
q2=bopdata[bopdata['fl2']=='Q2']
q2['merge']=q2['fl2']+" "+q2['year'].map(str)
#Select only columns required
q2gold=q2[['Exports','Imports','Balance','country','merge']]
q3=bopdata[bopdata['fl3']=='Q3']
q3['merge']=q3['fl3']+" "+q3['year'].map(str)
#Select only columns required
q3gold=q3[['Exports','Imports','Balance','country','merge']]
q4=bopdata[bopdata['fl4']=='Q4']
q4['merge']=q4['fl4']+" "+q4['year'].map(str)
#Select only columns required
q4gold=q4[['Exports','Imports','Balance','country','merge']]


gold1 = q1gold.append(q2gold, ignore_index=True)
gold2 = q3gold.append(gold1, ignore_index=True)
bopgold = q4gold.append(gold2, ignore_index=True)
bopgold['cnt']=1
bopgold2= bopgold.groupby(['country','merge'], as_index=False)['cnt','Exports','Imports','Balance'].sum()

#del bopgold2
#print bopgold2


cclist=[['AD','Andorra'],
['AE','United Arab Emirates'],
['AF','Afghanistan'],
['AG','Antigua and Barbuda'],
['AI','Anguilla'],
['AL','Albania'],
['AM','Armenia'],
['AO','Angola'],
['AQ','Antarctica'],
['BQ','Belarus4'],
['AR','Argentina'],
['AS','American Samoa'],
['AT','Austria'],
['AU','Australia'],
['AW','Aruba'],
['AX','Åland Islands'],
['AZ','Azerbaijan'],
['BA','Bosnia and Herzegovina'],
['BB','Barbados'],
['BD','Bangladesh'],
['BE','Belgium'],
['BF','Burkina Faso'],
['BG','Bulgaria'],
['BH','Bahrain'],
['BI','Burundi'],
['BJ','Benin'],
['BL','Saint Barthélemy'],
['BM','Bermuda'],
['BN','Brunei Darussalam'],
['BO','Bolivia, Plurinational State of'],
['BQ','Bonaire, Sint Eustatius and Saba'],
['CX','CEMAC'],
['BX','BIS3'],
['BR','Brazil'],
['BS','Bahamas'],
['BT','Bhutan'],
['BV','Bouvet Island'],
['BW','Botswana'],
['BY','Belarus'],
['BO','Bolivia'],
['WZ','WAEMU'],
['BZ','Belize'],
['CA','Canada'],
['CC','Cocos (Keeling) Islands'],
['CD','Congo, the Democratic Republic of the'],
['CF','Central African Rep.'],
['CG','Congo'],
['CH','Switzerland'],
['CI','Côte dIvoire'],
['CK','Cook Islands'],
['CL','Chile'],
['CM','Cameroon'],
['CN','China1'],
['CO','Colombia'],
['CR','Costa Rica'],
['CU','Cuba'],
['CV','Cabo Verde'],
['CW','Curaçao'],
['CX','Christmas Island'],
['CY','Cyprus'],
['CZ','Czech Republic'],
['EZ','ECB'],
['DE','Germany'],
['','Saudi Arabia'],
['DJ','Djibouti'],
['DK','Denmark'],
['DM','Dominica'],
['DO','Dominican Republic'],
['DZ','Algeria'],
['EC','Ecuador'],
['EE','Estonia'],
['EG','Egypt'],
['EH','Western Sahara'],
['ER','Eritrea'],
['ES','Spain'],
['ET','Ethiopia'],
['FI','Finland'],
['FJ','Fiji'],
['FK','Falkland Islands (Malvinas)'],
['FM','Micronesia, Federated States of'],
['FO','Faroe Islands'],
['FR','France'],
['GA','Gabon'],
['GB','United Kingdom of Great Britain and Northern Ireland'],
['IZ','IMF'],
['GD','Grenada'],
['GE','Georgia'],
['GF','French Guiana'],
['GG','Guernsey'],
['GH','Ghana'],
['GI','Gibraltar'],
['GL','Greenland'],
['GM','Gambia'],
['GN','Guinea'],
['GP','Guadeloupe'],
['GQ','Equatorial Guinea'],
['GR','Greece'],
['GS','South Georgia and the South Sandwich Islands'],
['GT','Guatemala'],
['GU','Guam'],
['GW','Guinea-Bissau'],
['GY','Guyana'],
['HK','Hong Kong'],
['HM','Heard Island and McDonald Islands'],
['HN','Honduras'],
['HR','Croatia'],
['HT','Haiti'],
['HU','Hungary'],
['ID','Indonesia'],
['IE','Ireland'],
['IL','Israel'],
['IM','Isle of Man'],
['IN','India'],
['IO','British Indian Ocean Territory'],
['IQ','Iraq'],
['IR','Iran, Islamic Republic of'],
['IS','Iceland'],
['IT','Italy'],
['JE','Jersey'],
['JM','Jamaica'],
['JO','Jordan'],
['JP','Japan'],
['KE','Kenya'],
['KG','Kyrgyz Republic'],
['KH','Cambodia'],
['KI','Kiribati'],
['KM','Comoros'],
['KN','Saint Kitts and Nevis'],
['KP','Korea'],
['KR','Korea, Republic of'],
['KW','Kuwait'],
['KY','Cayman Islands'],
['KZ','Kazakhstan'],
['LA','Laos'],
['LB','Lebanon'],
['LC','Saint Lucia'],
['LI','Liechtenstein'],
['LK','Sri Lanka'],
['LR','Liberia'],
['LS','Lesotho'],
['LT','Lithuania'],
['LU','Luxembourg'],
['LV','Latvia'],
['LY','Libya'],
['MA','Morocco'],
['MC','Monaco'],
['MD','Moldova, Republic of'],
['ME','Montenegro'],
['MF','Saint Martin (French part)'],
['MG','Madagascar'],
['MH','Marshall Islands'],
['MK','Macedonia'],
['',''],
['ML','Mali'],
['MM','Myanmar'],
['MN','Mongolia'],
['MO','Macao'],
['MP','Northern Mariana Islands'],
['MQ','Martinique'],
['MR','Mauritania'],
['MS','Montserrat'],
['MT','Malta'],
['MU','Mauritius'],
['MV','Maldives'],
['MW','Malawi'],
['MX','Mexico'],
['MY','Malaysia'],
['MZ','Mozambique'],
['NA','Namibia'],
['NC','New Caledonia'],
['NE','Niger'],
['NF','Norfolk Island'],
['NG','Nigeria'],
['NI','Nicaragua'],
['NL','Netherlands'],
['NO','Norway'],
['NP','Nepal'],
['NR','Nauru'],
['NU','Niue'],
['NZ','New Zealand'],
['OM','Oman'],
['PA','Panama'],
['PE','Peru'],
['PF','French Polynesia'],
['PG','Papua New Guinea'],
['PH','Philippines'],
['PK','Pakistan'],
['PL','Poland'],
['PM','Saint Pierre and Miquelon'],
['PN','Pitcairn'],
['PR','Puerto Rico'],
['PS','Palestine, State of'],
['RU','Russia'],
['PT','Portugal'],
['PW','Palau'],
['PY','Paraguay'],
['QA','Qatar'],
['RE','Réunion'],
['RO','Romania'],
['RS','Serbia'],
['RU','Russian Federation'],
['RW','Rwanda'],
['SA','Saudi Arabia2'],
['SB','Solomon Islands'],
['SC','Seychelles'],
['SD','Sudan'],
['SE','Sweden'],
['SG','Singapore'],
['SH','Saint Helena, Ascension and Tristan da Cunha'],
['SI','Slovenia'],
['SJ','Svalbard and Jan Mayen'],
['SK','Slovakia'],
['SL','Sierra Leone'],
['SM','San Marino'],
['SN','Senegal'],
['SO','Somalia'],
['SR','Suriname'],
['SS','South Sudan'],
['ST','Sao Tome and Principe'],
['SV','El Salvador'],
['SX','Sint Maarten (Dutch part)'],
['SY','Syrian Arab Republic'],
['SZ','Swaziland'],
['TC','Turks and Caicos Islands'],
['TD','Chad'],
['TF','French Southern Territories'],
['SY','Syria'],
['TG','Togo'],
['TH','Thailand'],
['TJ','Tajikistan'],
['TK','Tokelau'],
['TL','Timor-Leste'],
['TM','Turkmenistan'],
['TN','Tunisia'],
['TO','Tonga'],
['TR','Turkey'],
['TT','Trinidad and Tobago'],
['TV','Tuvalu'],
['TW','Taiwan'],
['',''],
['TZ','Tanzania, United Republic of'],
['UA','Ukraine'],
['',''],
['UG','Uganda'],
['UM','United States Minor Outlying Islands'],
['US','United States'],
['UK','United Kingdom'],
['UY','Uruguay'],
['UZ','Uzbekistan'],
['VA','Holy See'],
['',''],
['VC','Saint Vincent and the Grenadines'],
['VE','Venezuela, Bolivarian Republic of'],
['VG','Virgin Islands, British'],
['VI','Virgin Islands, U.S.'],
['VN','Viet Nam'],
['VE','Venezuela'],
['VU','Vanuatu'],
['WF','Wallis and Futuna'],
['WS','Samoa'],
['YE','Yemen'],
['',''],
['YT','Mayotte'],
['ZA','South Africa'],
['ZM','Zambia'],
['ZW','Zimbabwe']]
labels=['cc','country2']

country_list = pd.DataFrame.from_records(cclist, columns=labels)
country_list['country']=country_list['country2'].str.upper()
bigdata2=pd.merge(country_list, bigdata, left_on='country', right_on='country')

#Begin to delete columns
bigdata2.__delitem__('country2_x')
bigdata2.__delitem__('countryx')
bigdata2.__delitem__('country2_y')

bigdata3x=pd.merge(bigdata2, reserve,how='left',  left_on=['country','date'], right_on=['country','date'])
bigdata3=pd.merge(bopgold2, bigdata3x,how='left',  left_on=['country','merge'], right_on=['cc','quarter_y'])
bigdata3['dategold']=pd.to_datetime(bigdata3['date'], errors='coerce')
bigdata3['monthyear'] = bigdata3['dategold'].dt.strftime("%y%m")
bigdata3['FX Reserve2']=pd.to_numeric(bigdata3['FX Reserve'], errors='coerce')
bigdata3['Gold Tonne2']=pd.to_numeric(bigdata3['Gold Tonne'], errors='coerce')    
bigdata3[['country_x','Exports','Imports','Balance','merge','Gold Tonne','FX Reserve']]
#Build sort key
print bigdata3.dtypes

print bigdata3
result=tax_reciept.sort_index(ascending=False)
#Build a unique list to iterate through countries
print bigdata3.dtypes
countrylist=bigdata3['country_x']
cc=countrylist.drop_duplicates()

for i in cc:
    bigdata3['FXlagq']=bigdata3['FX Reserve2'].shift(1)
    bigdata3['FXlagy']=bigdata3['FX Reserve2'].shift(4)
    bigdata3['FXchange_qoverq']=bigdata3['FX Reserve2']-bigdata3['FXlagq']
    bigdata3['FXchange_yovery']=bigdata3['FX Reserve2']-bigdata3['FXlagy']
    bigdata3['GLDlagq']=bigdata3['Gold Tonne2'].shift(1)
    bigdata3['GLDlagy']=bigdata3['Gold Tonne2'].shift(4)
    bigdata3['GLDchange_qoverq']=bigdata3['Gold Tonne2']-bigdata3['GLDlagq']
    bigdata3['GLDchange_yovery']=bigdata3['Gold Tonne2']-bigdata3['GLDlagy']
    bigdata3['cnt']=1

#Build General Measures for the dataset
bigdata3['GLDchange_yovery_negfl'] = np.where(bigdata3['GLDchange_yovery']<0, 1, 0)
bigdata3['FXchange_yovery_negfl'] = np.where(bigdata3['FXchange_yovery']<0, 1, 0)
bigdata3['GLDchange_yovery_posfl'] = np.where(bigdata3['GLDchange_yovery']>0, 1, 0)
bigdata3['FXchange_yovery_posfl'] = np.where(bigdata3['FXchange_yovery']>0, 1, 0)

dfile= bigdata3.groupby(['monthyear'], as_index=False)['GLDchange_qoverq','GLDchange_yovery','FXchange_qoverq','FXchange_yovery','cnt','GLDchange_yovery_negfl','FXchange_yovery_negfl',\
'FXchange_yovery_posfl','GLDchange_yovery_posfl'].sum()
print dfile

print bigdata3.dtypes





#test=bigdata2.sort('country').drop_duplicates(subset=['country', 'cc'], take_last=True)
#print test


bigdata3.to_csv('C:\Python27\testbbb.csv'), index=False)
bigdata3.to_csv('testbbb.csv', index=False)
reserve.to_csv('testbbb2.csv', index=False)

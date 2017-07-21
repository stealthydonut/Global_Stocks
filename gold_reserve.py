#This script takes data from the world gold council and with simple transformation calculates the

import pandas
gold_df = pandas.read_csv("C:/Users/davking/Desktop/Python/gold.csv")
res_df = pandas.read_csv("C:/Users/davking/Desktop/Python/res.csv")
print res_df

#Generates the Gold Reserves for Each Country 
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
    df['date']=''.join(i[1])
    df['Gold Tonnes'] = df.loc[df['gold amount'].index, 'gold amount'].map(lambda x: x.replace('-','0'))
    df['country2'] = df.loc[df['countryx'].index, 'countryx'].map(lambda x: x.replace(')',''))
    df['country']=df['country2'].str.upper()
    bigdata = bigdata.append(df, ignore_index=False)

for i in colist:
    ticker=''.join(i[0])   
    df = res_df[['Unnamed: 0',ticker]]
    df.columns=['countryx','fxamount']
    df['date']=''.join(i[1])
    df['FX Reserve'] = df.loc[df['fxamount'].index, 'fxamount'].map(lambda x: x.replace('-','0'))
    df['country2'] = df.loc[df['countryx'].index, 'countryx'].map(lambda x: x.replace(')',''))
    df['country']=df['country2'].str.upper()
    reserve = reserve.append(df, ignore_index=False)

    
#print reserve

#del bigdata

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
['','Kyrgyz Republic'],
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

bigdata3=pd.merge(bigdata2, reserve, left_on='country', right_on='country')
bigdata3['date']=pd.to_datetime(bigdata3['date_y'], errors='coerce')
bigdata3['monthyear'] = bigdata3['date'].dt.strftime("%m%y")

countrylist=bigdata3['country']
cc=countrylist.drop_duplicates()

for i in cc:
    bigdata3['FXlagq']=bigdata3['FX Reserve'].shift(1)
    bigdata3['FXlagy']=bigdata3['FX Reserve'].shift(4)
    bigdata3['GLDlagq']=bigdata3['Gold Tonnes'].shift(1)
    bigdata3['GLDlagy']=bigdata3['Gold Tonnes'].shift(4)



print bigdata3

dfile = bigdata3.groupby(['country','monthyear'], as_index=False)['Gold Tonnes','FX Reserve'] 

print dfile.dtype

print countrylist

print bigdata3
print bigdata3.dtypes





#test=bigdata2.sort('country').drop_duplicates(subset=['country', 'cc'], take_last=True)
#print test


bigdata3.to_csv('C:\Python27\gold_reserve.csv', index=False)


#Sourced from the following site https://github.com/mortada/fredapi
import pandas as pd
cclist=['TRESEGCAM052N','CA'],['TRESEGCNM052N','CN'],['TRESEGSAM194N','SA']


from fredapi import Fred
fred = Fred(api_key='4af3776273f66474d57345df390d74b6')

reserve = pd.DataFrame()


for i in test:
    try:
        part1='TRESEG'
        part2=''.join(i[0]) 
        part3='M052N'
        value=part1+part2+part3
        data2 = fred.get_series_all_releases(value)
        data2['reserves']=pd.to_numeric(data2['value'], errors='coerce')
        data2['date2']=pd.to_datetime(data2['date'], errors='coerce')
        data2['cc']=part2
        data2['source']=value     
        reserve = reserve.append(data2, ignore_index=False)
    except:
        print i

reservex=reserve.sort_values(['date2','cc'], ascending=[True, True])
reservex['reserves_mm']=reservex['reserves']/1000000
reservex2=reservex[reservex['reserves_mm'].notnull()]
reservex3=reservex2.drop_duplicates(['date2','cc'], keep='last')    
        
        

print reservex3
del reserve
del reservex
del data2

cclist=[['AD','Andorra'],
['AE','United Arab Emirates'],
['AF','Afghanistan'],
['AG','Antigua and Barbuda'],
['AI','Anguilla'],
['AL','Albania'],
['AM','Armenia'],
['AO','Angola'],
['AQ','Antarctica'],
['BY','Belarus4'],
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
['CD','Congo'],
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
['ES','Estonia'],
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
['ES','El Salvador'],
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
['GB','United Kingdom'],
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

#######################################
#Get the reserve data for all countries
#######################################

reserve = pd.DataFrame()

for i in cclist:
    try:
        part1='TRESEG'
        part2=''.join(i[0]) 
        part3='M052N'
        value=part1+part2+part3
        data2 = fred.get_series_all_releases(value)
        data2['reserves']=pd.to_numeric(data2['value'], errors='coerce')
        data2['date2']=pd.to_datetime(data2['date'], errors='coerce')
        data2['cc']=part2
        data2['source']=value   
        data2['type']='Reserves' 
        reserve = reserve.append(data2, ignore_index=False)
    except:
        print i

reservex=reserve.sort_values(['date2','cc'], ascending=[True, True])
reservex['reserves_mm']=reservex['reserves']/100000000
reservex2=reservex[reservex['reserves_mm'].notnull()]
reservex3=reservex2.drop_duplicates(['date2','cc'], keep='last')    
reservex3['cnt']=1
        
#######################################
#Get the SDR data for all countries
#######################################

sdr = pd.DataFrame()

for i in cclist:
    try:
        part1='TRESEG'
        part2=''.join(i[0]) 
        part3='M194N'
        value=part1+part2+part3
        data2 = fred.get_series_all_releases(value)
        data2['sdr amt']=pd.to_numeric(data2['value'], errors='coerce')
        data2['date2']=pd.to_datetime(data2['date'], errors='coerce')
        data2['cc']=part2
        data2['source']=value
        data2['type']='SDR'     
        sdr = sdr.append(data2, ignore_index=False)
    except:
        print i


sdrx=sdr.sort_values(['date2','cc'], ascending=[True, True])
sdrx['sdr_mm']=sdrx['sdr amt']/100000000
sdrx2=sdrx[sdrx['sdr_mm'].notnull()]
sdrx3=sdrx2.drop_duplicates(['date2','cc'], keep='last')    
sdrx3['cnt']=1          


     
     





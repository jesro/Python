import csv
import pandas
import re
import math
p = pandas.read_csv('Product_Load.csv',encoding="ISO-8859-1")
p['PICGROUP_TEXT_BODY']=p['PICGROUP_TEXT_BODY'].str.replace('<.*?>', '')
m = p.groupby('SUBCAT_DESC').apply(lambda x: x.iloc[: math.floor(x.SUBCAT_DESC.size*0.7)] if x.SUBCAT_DESC.size > 5 else x.iloc[:6])
m['PICGROUP_TEXT_BODY'].to_csv('training.csv')
n = p.groupby('SUBCAT_DESC').apply(lambda x: x.iloc[math.floor(x.SUBCAT_DESC.size*0.7):math.floor(x.SUBCAT_DESC.size*0.9)] if x.SUBCAT_DESC.size > 5 else None)
n['PICGROUP_TEXT_BODY'].to_csv('test.csv')
o = p.groupby('SUBCAT_DESC').apply(lambda x: x.iloc[math.floor(x.SUBCAT_DESC.size*0.9):] if x.SUBCAT_DESC.size > 5 else None)
o['PICGROUP_TEXT_BODY'].to_csv('validation.csv')
#m['PICGROUP_TEXT_BODY'].equals(n['PICGROUP_TEXT_BODY'])
#for i in p['PICGROUP_TEXT_BODY'].isin(m['PICGROUP_TEXT_BODY']): 
#    if i:
#       print('yes')

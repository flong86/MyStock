import easytrader
from datetime import datetime
from datetime import timedelta
import os
user = easytrader.use('ht', False)
user.prepare('ht.json')     
##print(user.position)

#获取组合最近5次调仓
#user.entrust())

#获取最近30天交割单
#print(user.exchangebill)

#获取交割单
starttime = datetime(2015, 1, 1)
print(starttime.strftime('%Y%m%d'))
endtime = starttime
mon = timedelta(days =30)
now = datetime.now()

#写入本地文件
filepath = '..\\data\\bill.csv'
if (os.path.exists(filepath)):
    f = open(filepath, 'wt')
else:
    f = open(filepath, 'xt')

##if f is not None:
##    f.write("qewqw")
##f.close()

while(endtime < now):
    starttime = endtime
    print(starttime)
    
    endtime = endtime + mon
    if endtime >= now:
        endtime = now
    print(endtime)
    bill = user.get_exchangebill(starttime.strftime('%Y%m%d'), endtime.strftime('%Y%m%d'))
    try:
        if bill['item'] is None:
            print('No Data')
            continue
    except:
        pass   
  
    for c in bill:
        str1 = c['date'] + ','
        str1 += c['business_name'] +','
        str1 += c['stock_code']+','
        str1 += c['stock_name']+ ','
        str1 += str(c['business_price'])+ ','
        str1 += str(c['occur_amount'])+ ','
        str1 += str(c['business_balance'])+ ','
        str1 += str(c['occur_balance'])+','
        str1 += str(c['fare0']) +','
        str1 += c['entrust_no']+','
        str1 += c['stock_account']+'\n'
        
        #print(c["date"])
        #print(str1)
        #print(c['item'])
        #print(c)
        #print(eval(c))
        f.write(str1)
        #print(bill)
        #print('\n\t')
f.close()
    






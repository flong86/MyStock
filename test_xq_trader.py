import easytrader
import time

print(time.time())
inttime = 1467343084

print(time.localtime(inttime))
print(time.localtime(time.time()))


user = easytrader.use('yjb', True)
user.prepare('yjb.json')   
user.buy('002605', price=17.94, amount=100)


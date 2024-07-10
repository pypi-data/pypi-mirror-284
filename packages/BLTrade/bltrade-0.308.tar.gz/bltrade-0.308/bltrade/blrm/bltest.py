from tqsdk import TqAccount, TqApi, TqAuth,TqSim

import datetime
import blrmcore
import pandas as pd

#api = TqApi(TqAccount("C创元期货", "13000252", "jwz20230301"), auth=TqAuth("billin", "dnadna"))

api = TqApi(TqSim(), auth=TqAuth('billin', 'dnadna'))



account = api.get_account()
print(account.balance)
print(account.float_profit)

#position = api.get_position("SHFE.ag2408")
position = api.get_position()
print("----------------position---------------")
print(position)

# 时间检测测试
#t=datetime.time(9,0)
t=datetime.time(13,23)
print("开始时间",t)
t2=datetime.datetime.now()
print("现在时间",t2.time())
if t<t2.time():
    print("现在时间晚于开始时间")
else:
    print("现在时间早于开始时间")

#quote测试
quote1 = api.get_quote("SHFE.ag2408")

#order1 = api.insert_order(symbol="SHFE.ag2408", direction="BUY", offset="OPEN", limit_price=quote1.ask_price1, volume=2)
# 买更便宜的
order1 = api.insert_order(symbol="SHFE.ag2408", direction="BUY", offset="OPEN", limit_price=quote1.ask_price1-2, volume=2)
"""
while order1.status != "FINISHED":
    api.wait_update()
    print("order1 opend")
"""

quote2 = api.get_quote("SHFE.ru2409")
order2 = api.insert_order(symbol="SHFE.ru2409", direction="BUY", offset="OPEN", limit_price=quote2.ask_price1, volume=2)
# 买更便宜的
#order2 = api.insert_order(symbol="SHFE.ru2409", direction="BUY", offset="OPEN", limit_price=quote2.ask_price1-2, volume=2)
#api.cancel_order(order2)
orders=api.get_order()
#print(orders)
for i,o in orders.items():
    #print("i=",i,"o=",o)
    if o['status']=="ALIVE":
        api.cancel_order(o)

#df=pd.DataFrame(orders.values())
#df=df[df['status']=='ALIVE']
#print("df=",df)


"""
while order2.status != "FINISHED":
    api.wait_update()
    print("order2 opend")
"""

print("----------------开始调用一键平仓------------------------------------------------------")
blrmcore.blEmpty(api)


print("----------------平仓后仓位信息------------------------------------------------------")
for n,p in position.items():
    #print("name=",n,"p=",p)
    print("品种:",n,"浮盈：",p.float_profit_long + p.float_profit_short,"   多仓:",p.pos_long,"空仓:",p.pos_short,)
    quote = api.get_quote(n)
    #print(quote)
    print("合约代码：",quote.instrument_id,"卖1:",quote.ask_price1,"买1:",quote.bid_price1)
    

print("账户资金：",account.balance,"账户浮盈:",account.float_profit)


"""
# 监控程序主循环
# 这里依赖一个前面活跃的quote来触发每次循环
while api.wait_update():
    print("----------------kv------------------------------------------------------")
    for n,p in position.items():
        #print("name=",n,"p=",p)
        print("品种:",n,"浮盈：",p.float_profit_long + p.float_profit_short,"   多仓:",p.pos_long,"空仓:",p.pos_short,)
        quote = api.get_quote(n)
        #print(quote)
        print("合约代码：",quote.instrument_id,"卖1:",quote.ask_price1,"买1:",quote.bid_price1)

    print("账户资金：",account.balance,"账户浮盈:",account.float_profit)

"""


"""
order = api.insert_order(symbol="SHFE.ag2408", direction="SELL", offset="CLOSETODAY", limit_price=quote.bid_price1,
                         volume=2)

while order.status != "FINISHED":
    api.wait_update()
print("closed")
"""
api.close()

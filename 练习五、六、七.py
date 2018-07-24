# -*- coding: utf-8 -*-
"""


"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:02:03 2018
练习五：
                    1.练习4使用到函数，使用到list的一些功能
                    2.优化代码，用函数的方式修改练习4，输出每一天的天气（函数）
                    3.打印温度折线图，使用函数优化（必须要有返回值）
@author: JinF
"""

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
def weather(d,a):
    print('this day is'+str(d)+'天的天气情况')
    print('情况：'+str(data['list'][a]['weather'][0]['main']))
weather(2,1)
weather(10,2)
weather(18,3)
weather(26,4)
weather(34,5)
#2
def A(a):
    data1=data['list'][a]['main']['temp']
    num=str('-')*int(data1)
    return num
print('day1'+A(1))
print('day2'+A(2))
print('day3'+A(3))
print('day4'+A(4))
print('day5'+A(5))



# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:09:26 2018
 练习六
                    1.显示4个商品，然后打印分割线，只要第一页36个商品信息
                    2.列出36个商品
                    3.获取所有的商品价格并给商品排序，从高到低
                    4.按照销量排序
                    5.商品过滤，只要15天退款或者包邮的商品信息，显示

@author: JinF
"""
url='https://s.taobao.com/search?q=qunzi&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
#第一、二题
for i in range(0,4):    
    print('第{}件商品'.format(i+1))
    print(data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    print(data['mods']['itemlist']['data']['auctions'][i]['nick'])
print('-'*10)
for i in range(0,36):    
    print('第{}件商品'.format(i+1))
    print(data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    print(data['mods']['itemlist']['data']['auctions'][i]['nick'])              
    if (i+1)%4==0:
         print('-'*10)
#第三题
ls=[]
def price():
    for i in range(0,36):                                                                                                               
      p=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
      print('')
      ls.append(p)
    return ls
price()
a=sorted(ls)
print('商品价格排序为：')
b=list(reversed(a))
print(b)  
#第四题
ls1=[]
for t in range(0,36):       
    m=str(data['mods']['itemlist']['data']['auctions'][t]['view_sales'])
    x=int(m[0:-3])
    ls1.append(x)
y=sorted(ls1)
s=list(reversed(y))
print('商品销量从高到低为：'+str(s))
#第五题
print('包邮的商品为：')
def F(i):   
    print('第'+format(i+1)+'个商品')
    print(data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    print(data['mods']['itemlist']['data']['auctions'][i]['nick'])              
    print('-'*10)
for i in range(0,36):   
    if float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])==0:   
      F(i)
        





# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:49:34 2018
#练习题七
1.使用多选其一，完成天气的提醒（if），淘宝客服端
2.一定要多次使用for循环，偶尔使用while循环，在淘宝客户端
3.使用到break或者continue
#练习题八  保存淘宝数据（小组项目）
1.每个组员爬取某个商品的100页数据，每个组员爬取的不同的城市，组间城市不重复
2.保存淘宝商品信息（同练习题6），并且保存为CSV格式
3.每组组长合并各组员的数据  后续班级合并

@author: JinF
"""
#天气情况
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
#1.打印每天18点的天气信息，温度，程序，
def Advise(a):  
    if a=='Clear': 
      print('Advise:晴天注意防晒')
    elif a=='Clouds':
      print('Advise:多云出去走走')
    elif a=='Rain':
      print('Advise:雨天记得带伞')
def weather(d): 
    print('第'+str(d)+'天:')
    i=2+(int(d)-1)*8
    print('温度'+str(data['list'][i]['main']['temp']))
    print('情况'+str(data['list'][i]['weather'][0]['main']))
    print('气压'+str(data['list'][i]['main']['pressure']))
    print('最高温度'+str(data['list'][i]['main']['temp_max']))
    print('最低温度'+str(data['list'][i]['main']['temp_min']))
    Advise(str(data['list'][i]['weather'][0]['main']))
for d in range(1,5):
    weather(d)
def chart(d):   
    i=2+(int(d)-1)*8
    b='-'*int(data['list'][i]['main']['temp'])
    return b
print('折线图为：')  
for d in range(1,5):    
    print(chart(d))
#淘宝客户端
url='https://s.taobao.com/search?q=qunzi&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
for i in range(0,36):
    if i==5:break
    elif i==10:continue
    print('第{}件商品'.format(i+1))
    print(data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    print(data['mods']['itemlist']['data']['auctions'][i]['nick'])              
    if (i+1)%4==0:
         print('-'*10)
    

    

    

        
    


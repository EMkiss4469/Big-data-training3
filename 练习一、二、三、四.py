# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:53:59 2018

@author: JinF
"""

#习题一：
"""
    1.定义一个天气温度列表写出里面每一天的温度
    2.打印一周的天气，天气里面的周三打印除外：周三+温度
"""
a=['23℃','25℃','30℃','31℃','32℃','31℃','34℃']
print(a[0]+' '+a[1]+' '+'周三:'+a[2]+' '+a[3]+' '+a[4]+' '+a[5]+' '+a[6])

#习题二：
"""
    1.定义一个字典，里面存储五天的天气信息，有温度，天气情况
    2.打印星期三的温度和天气情况
"""
b={'周一':['23℃','小雨'],
   '周二':['35℃','晴'],
   '周三':['21℃','阵雨'],
   '周四':['23℃','大风'],
   '周五':['23℃','小雨']}
print(b['周三'])

#习题三：
"""
    1.通过复制联网天气代码，获取老家的天气字典
    2.打印温度temp,天气情况description，天气气压pressure
"""
import urllib.request as r #导入联网工具包， 打开网址，读取内容转换为str
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=sichuan&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
import json#字符串转字典的工具包
data=json.loads(data)

print(data['main']['temp'])
print(data['weather'][0]['description'])
print(data['main']['pressure'])

#练习题四
""" 
    1.打印每天18点的天气信息，温度，程序，情况，气压，最高温度，最低温度
    2.写出英文版的天气-天气情况，用户输入英文   application应用
    3.打印温度折线图
        1----------
        2--------------------
        3-------
        4----------
    4.获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
    5.友情提示，根据温度提示穿衣，打伞，出门(可选)'''
"""  
#问题一
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

print('第一天18点:')
print('温度:'+str(data['list'][2]['main']['temp']))
print('气压:'+str(data['list'][2]['main']['pressure']))
print('情况:'+str(data['list'][2]['weather'][0]['main']))
print('最低气温:'+str(data['list'][2]['main']['temp_min']))
print('最高气温:'+str(data['list'][2]['main']['temp_max']))
print('  ')
print('第二天18点:')
print('温度:'+str(data['list'][10]['main']['temp']))
print('气压:'+str(data['list'][10]['main']['pressure']))
print('情况:'+str(data['list'][10]['weather'][0]['main']))
print('最低气温:'+str(data['list'][10]['main']['temp_min']))
print('最高气温:'+str(data['list'][10]['main']['temp_max']))
print('  ')
print('第三天18点:')
print('温度:'+str(data['list'][18]['main']['temp']))
print('气压:'+str(data['list'][18]['main']['pressure']))
print('情况:'+str(data['list'][18]['weather'][0]['main']))
print('最低气温:'+str(data['list'][18]['main']['temp_min']))
print('最高气温:'+str(data['list'][18]['main']['temp_max']))
print('  ')
print('第四天18点:')
print('温度:'+str(data['list'][26]['main']['temp']))
print('气压:'+str(data['list'][26]['main']['pressure']))
print('情况:'+str(data['list'][26]['weather'][0]['main']))
print('最低气温:'+str(data['list'][26]['main']['temp_min']))
print('最高气温:'+str(data['list'][26]['main']['temp_max']))
print('  ')
print('第五天18点:')
print('温度:'+str(data['list'][34]['main']['temp']))
print('气压:'+str(data['list'][34]['main']['pressure']))
print('情况:'+str(data['list'][34]['weather'][0]['main']))
print('最低气温:'+str(data['list'][34]['main']['temp_min']))
print('最高气温:'+str(data['list'][34]['main']['temp_max']))

#问题二
input=input('Please input city:')
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'.format(input)
data=r.urlopen(url).read().decode('utf-8','ignore')
data=json.loads(data)
print('{} weather:'.format(input))
print('This weather in first day:')
print('temperature:'+str(data['list'][2]['main']['temp']))
print('pressure:'+str(data['list'][2]['main']['pressure']))
print('description:'+str(data['list'][2]['weather'][0]['main']))
print('temp_min:'+str(data['list'][2]['main']['temp_min']))
print('temp_max:'+str(data['list'][2]['main']['temp_max']))
print('  ')
print('This weather in second day:')
print('temperature:'+str(data['list'][10]['main']['temp']))
print('pressure:'+str(data['list'][10]['main']['pressure']))
print('description:'+str(data['list'][10]['weather'][0]['main']))
print('temp_min:'+str(data['list'][10]['main']['temp_min']))
print('temp_max:'+str(data['list'][10]['main']['temp_max']))
print('  ')
print('This weather in third day:')
print('temperature:'+str(data['list'][18]['main']['temp']))
print('pressure:'+str(data['list'][18]['main']['pressure']))
print('temp_min:'+str(data['list'][18]['main']['temp_min']))
print('temp_max:'+str(data['list'][18]['main']['temp_max']))
print('  ')
print('This weather in forth day:')
print('temperature:'+str(data['list'][26]['main']['temp']))
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('description:'+str(data['list'][26]['weather'][0]['main']))
print('temp_min:'+str(data['list'][26]['main']['temp_min']))
print('temp_max:'+str(data['list'][26]['main']['temp_max']))
print('  ')
print('This weather in five day:')
print('temperature:'+str(data['list'][34]['main']['temp']))
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('description:'+str(data['list'][34]['weather'][0]['main']))
print('temp_min:'+str(data['list'][34]['main']['temp_min']))
print('temp_max:'+str(data['list'][34]['main']['temp_max']))


#问题三
data1=data['list'][2]['main']['temp']
data2=data['list'][10]['main']['temp']
data3=data['list'][18]['main']['temp']
data4=data['list'][26]['main']['temp']
data5=data['list'][34]['main']['temp']
num1=str('-')*int(data1)
num2=str('-')*int(data2)
num3=str('-')*int(data3)
num4=str('-')*int(data4)
num5=str('-')*int(data5)
print('这五天温度的折线图：')
print('   1'+num1)
print('   2'+num2)
print('   3'+num3)
print('   4'+num4)
print('   5'+num5)

#问题四
list=[data1,data2,data3,data4,data5]
print('这五天天气温度从低到高排序：')
print(sorted(list[1:5]))

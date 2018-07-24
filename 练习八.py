# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:09:34 2018
 练习题八  保存淘宝数据（小组项目）
                    1.每个组员爬取某个URL的100页数据，每个组员爬取的不同的城市，组间城市不重复
                    2.保存淘宝商品信息（同练习题6），并且保存为CSV格式
                    3.每组组长合并各组员的数据  后续班级合并
@author: JinF
"""
import urllib.request as r
f=open('安徽裙子淘宝数据.csv','w',encoding='gbk')
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E5%AE%89%E5%BE%BD&s={}&ajax=true'
for i in range(0,100):
    s=0+i*44
    url1=url.format(s)
    try:
        data=r.urlopen(url1).read().decode('utf-8','ignore')#bytes-->str
        f.write(data+'\n')
        print('第{}页商品信息'.format(i))
    except Exception as err:
        print('错误')
    

f.close ()


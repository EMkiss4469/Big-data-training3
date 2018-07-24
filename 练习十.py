
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:25:09 2018
习题10：
1、获取2300所学校的编号
2、获取31所城市的编号
3、获取142600数据，31/10，每个组3个城市数据，后面组装在一起
4、将142600数据用spark统计
@author: JinF
"""
#1、获取2300所学校的编号
#获取142600数据，31/10，每个组3个城市数据，后面组装在一起
ls=open('C:/Users/JinF/Desktop/all_school.txt',encoding='utf-8').readlines()
schoolls=[]
for line in ls: 
    s=line.split('-jianjie-')[1]
    s=s.split('.')[0]
    schoolls.append(s)
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={
        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }
f=open('全国招生人数.txt','a',encoding='utf-8')
print('学校编号为：')
for schoolid in schoolls:   
     try:   
        req=r.Request(url,data='id={}&type=1&city=13&state=1'.format(schoolid).encode(),headers=headers)  
        d=r.urlopen(req).read().decode('utf-8','ignore')
        if d.startswith("{"):
            f.write(d+"\n")
            print(schoolid)
        else:
            print('网址出错'+schoolid)
     except Exception as err:  
           print('此行有误')
      
f.close()
#3、获取142600数据，31/10，每个组3个城市数据，后面组装在一起
f2=open('C:/Users/JinF/Desktop/大数据实训/XML高考派城市.txt',encoding='gbk').readlines()
print('31所城市编号为：\n')
for k in range(1,32): 
    print(f2[k].split('<li data-val="')[1].split('" data-id=')[0]+':'+f2[k].split('claimCity')[1].split(',')[1].split(')">')[0])
f2.close()
'''idea(scala文件)
//4、将142600数据用spark统计
import scala.collection.mutable.ListBuffer

/**
  * 1.读取文件textFile
  * 2.过滤"status":0}的数据 filter
  * 3.将 "data":Array[5]转变成多行  flatMap   抚平
  * 4.获取 "school":"华南师范大学",  "plan":"2",
  * 4.获取 "school":"华南师范大学",  "plan":"2",  reduce 缩减
  * 5.学校和招生人数 排序， 按照招生人数排序 。sort
  *
  */
object YaSpark1{
  def main(args: Array[String]) {
    import org.json.JSONObject//导入str转json工具包
    import org.apache.spark.SparkConf//
    import org.apache.spark.SparkContext
    //sparkcontext的配置，运行在本地，名称为cala
    val conf = new SparkConf().setAppName("cala").setMaster("local").set("spark.testing.memory","2147480000");
    val sc = new SparkContext(conf)//Spark运行环境,,本地电脑，集群
    //使用spark读取文本文件
    sc.textFile("河北文科招生人数.txt")
      .filter(line=>line.endsWith("status\":1}"))
      .flatMap(line=>{//line str===>List line  抚平
      val  json = new JSONObject(line)
        val jsonlist = json.getJSONArray("data")
        //        jsonlist.getJSONObject(0)
        val list = ListBuffer[JSONObject]()
        for(i<-0 to jsonlist.length()-1){
          list.append(jsonlist.getJSONObject(i))
        }
        list
      })
      .map(line=>(line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line=>println(line))

  }
}
object YaSparkTest{
  def main(args: Array[String]) {
    println("aaa@qq.com".endsWith("qq.com"))
    println("status\":1}")
    //    new JsonObject
    //    import json    将字符串转换为json（字典）
    import org.json.JSONObject
    val json = new JSONObject("{\"data\":{\"city_name\":\"\\u6e56\\u5357\"},\"info\":\"\",\"status\":0}")
    println(json.getInt("status"))
    println(json.getJSONObject("data"))
    val list = List[Int](1,1,1)//大小不变的固定列表
    //    list(2) = 3
    val list2 = ListBuffer[Int]()
    list2.append(3)
    list2.append(4)
    println(list2)
  }
}
'''
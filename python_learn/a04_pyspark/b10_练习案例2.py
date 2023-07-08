"""    
    @author: fosss
    Date: 2023/7/8
    Time: 16:48
    Description:完成三个需求
"""
import json

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 需求1：各个城市销售额排名，从大到小
order_rdd = sc.textFile("E:/fo的python学习/python_learn/a04_pyspark/orders.txt")
# 将每个json分开
order_rdd = order_rdd.flatMap(lambda x: x.split('|'))
# 转成字典，便于取值
dict_rdd = order_rdd.map(lambda x: json.loads(x))
# 组装k,v 并进行聚合
map_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))  # 此处不要忘了转成数字，用于后面的相加操作
# print(map_rdd.collect())
rbk_rdd = map_rdd.reduceByKey(lambda x, y: x + y)
# print(rbk_rdd.collect())
# # 排名
res1 = rbk_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print("需求1：", res1.collect())

# 需求2：全部城市，有哪些商品类别在售卖
# 先获取所有的商品，再进行去重
res2 = dict_rdd.map(lambda x: x['category']).distinct()
print("需求2：", res2.collect())
# 北京市有哪些商品类别在售卖
# 过滤处北京市的商品
res3 = dict_rdd.filter(lambda x: x['areaName'] == '北京').map(lambda x: x['category']).distinct()
print("需求3：", res3.collect())

sc.stop()
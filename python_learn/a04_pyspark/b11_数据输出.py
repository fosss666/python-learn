"""    
    @author: fosss
    Date: 2023/7/8
    Time: 18:01
    Description:
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize("afjaojfoiajfa")

# 1.collect算子输出列表
print(rdd.collect(), type(rdd.collect()))

# 2.reduce算子输出和
rdd2 = sc.parallelize([1, 2, 3, 4, 5])
print(rdd2.reduce(lambda x, y: x + y))

# 3.take算子输出前几个元素组成的集合
print(rdd.take(3))
#
# # 4.count算子输出元素数量
print(rdd.count())

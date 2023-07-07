"""    
    @author: fosss
    Date: 2023/7/7
    Time: 19:05
    Description:统计文件文本中各单词出现的次数
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

hello_rdd = sc.textFile("E:/fo的python学习/python_learn/a04_pyspark/hello.txt")

hello_rdd = hello_rdd.flatMap(lambda x: x.split(' '))

# 转成k,v形式
hello_rdd_with_one = hello_rdd.map(lambda x: (x, 1))
# print(hello_rdd_with_one.collect())

# 进行统计
res_rdd = hello_rdd_with_one.reduceByKey(lambda x, y: x + y)
print(res_rdd.collect())

sc.stop()

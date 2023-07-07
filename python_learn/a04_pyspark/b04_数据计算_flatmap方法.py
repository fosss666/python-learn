"""    
    @author: fosss
    Date: 2023/7/7
    Time: 14:32
    Description:flagmap相较于map，会自动解除嵌套存储的嵌套
"""
from pyspark import SparkConf, SparkContext
# 需要为spark指定python解释器的位置
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

# rdd = sc.parallelize([[1, 2, 3], [4, 5, 6]])
rdd = sc.parallelize(["1,2,3", "4,5,6"])
# rdd = rdd.map(lambda x: x.split(','))
rdd = rdd.flatMap(lambda x: x.split(','))

print(rdd.collect())

sc.stop()

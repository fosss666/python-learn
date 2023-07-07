"""    
    @author: fosss
    Date: 2023/7/7
    Time: 13:41
    Description:
"""
from pyspark import SparkConf, SparkContext
# 需要为spark指定python解释器的位置
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd = rdd.map(lambda x: x * 10 + 5).map(lambda x: x * 1)
print(rdd.collect())

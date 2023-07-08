"""    
    @author: fosss
    Date: 2023/7/8
    Time: 16:23
    Description:distinct用于去重
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 1, 1, 2, 2, 3, 2, 3, 4, 5])

rdd2 = rdd.distinct()
print(rdd2.collect())

sc.stop()

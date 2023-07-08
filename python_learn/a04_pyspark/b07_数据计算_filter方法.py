"""    
    @author: fosss
    Date: 2023/7/8
    Time: 16:15
    Description:
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'
conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

rdd2 = rdd.filter(lambda x: x % 2 == 0)
print(rdd2.collect())

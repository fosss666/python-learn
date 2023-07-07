"""    
    @author: fosss
    Date: 2023/7/7
    Time: 18:17
    Description:数据为k,v型  根据提供的函数进行聚合运算
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('上', 11), ('左', 22), ('上', 33), ('左', 44)])

rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())

"""    
    @author: fosss
    Date: 2023/7/8
    Time: 18:21
    Description:
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['HADOOP_HOME'] = 'F:/hadoop-3.0.0'

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize("afjaojfoiajfa", numSlices=1)  # numSlices=1表示：输出的文本放到一个文件中

rdd.saveAsTextFile('./output')

sc.stop()

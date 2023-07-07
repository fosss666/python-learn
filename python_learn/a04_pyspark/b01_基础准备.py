"""    
    @author: fosss
    Date: 2023/7/7
    Time: 11:28
    Description:
"""
from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
conf = SparkConf().setMaster('local[*]').setAppName("test_spark_app")
# 基于SparkConf创建SparkContext对象
sc = SparkContext(conf=conf)
# 打印Spark版本
print(sc.version)
# 关闭Spark
sc.stop()

"""    
    @author: fosss
    Date: 2023/7/8
    Time: 16:30
    Description:排序
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
# print(res_rdd.collect())

# 排序
"""第一个参数指明依据元组那个元素进行排序，第二个参数控制是否升序，第三个参数暂未知"""
res = res_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(res.collect())

sc.stop()

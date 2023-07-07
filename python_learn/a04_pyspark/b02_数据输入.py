"""    
    @author: fosss
    Date: 2023/7/7
    Time: 12:30
    Description:
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
sc = SparkContext(conf=conf)

# 读取python对象转成rdd
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize({1, 2, 3, 4, 5})
rdd4 = sc.parallelize("1,2,3,4,5")
rdd5 = sc.parallelize({"k1": "v1", "k2": "v2"})

# 输出内容
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# 读取文件转为rdd对象
rdd = sc.textFile("E:/fo的python学习/python_learn/a04_pyspark/hello.txt")
print(rdd.collect())
# 停止spark
sc.stop()

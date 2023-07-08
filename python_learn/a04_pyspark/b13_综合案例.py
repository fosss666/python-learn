"""    
    @author: fosss
    Date: 2023/7/8
    Time: 19:14
    Description:
"""
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = 'F:/python/python.exe'

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

file_rdd = sc.textFile("E:/fo的python学习/python_learn/a04_pyspark/search_log.txt")

# 打印输出：热门搜索时间段（小时精度）Top3
res1 = file_rdd.map(lambda x: (x.split('\t')[0][:2], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
print(res1)
# 打印输出：热门搜索词Top3
res2 = file_rdd.map(lambda x: (x.split('\t')[2], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
print(res2)
# 打印输出：统计黑马程序员关键字在哪个时段被搜索最多

# res3 = file_rdd.map(lambda x: x.split('\t')). \
#     map(lambda x: {'time': x[0], 'user_id': x[1], 'key_word': x[2], 'rank1': x[3], 'rank2': x[4], 'url': x[5]}). \
#     filter(lambda x: x['key_word'] == '黑马程序员'). \
#     map(lambda x: (x['time'][:2], 1)). \
#     reduceByKey(lambda x, y: x + y). \
#     sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
#     take(1)

res3 = file_rdd.map(lambda x: x.split('\t')). \
    filter(lambda x: x[2] == '黑马程序员'). \
    map(lambda x: (x[0][:2], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(1)
print(res3)
# 将数据转换为JSON格式，写出为文件

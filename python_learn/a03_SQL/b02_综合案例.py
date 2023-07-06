"""    
    @author: fosss
    Date: 2023/7/6
    Time: 17:27
    Description:
"""
from pymysql import Connection
from a02_面向对象.b13_数据分析案例 import file_define

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)
conn.select_db('py_sql')

cursor = conn.cursor()

# 读取数据
f1 = file_define.TextFileReader("E:/fo的python学习/python_learn/a02_面向对象/b13_数据分析案例/2011年1月销售数据.txt")
f2 = file_define.JsonFileReader(
    "E:/fo的python学习/python_learn/a02_面向对象/b13_数据分析案例/2011年2月销售数据JSON.txt")
jan_data = f1.read()
feb_data = f2.read()
# 合成一个数据
all_data = jan_data + feb_data
for record in all_data:
    sql = f"insert into data(time,order_id,money,province) values('{record.date}','{record.order_id}','{record.money}','{record.province}')"
    cursor.execute(sql)
# 提交事务
conn.commit()

conn.close()

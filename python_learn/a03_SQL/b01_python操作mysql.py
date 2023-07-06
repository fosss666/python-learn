"""    
    @author: fosss
    Date: 2023/7/6
    Time: 16:27
    Description:
"""
from pymysql import connections

conn = connections.Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)
# print(conn.get_server_info(), conn.get_host_info(), conn.get_proto_info())

# 选择数据库
conn.select_db("dg_test")
# 获取游标对象
cursor = conn.cursor()

# 执行sql语句
cursor.execute("insert into student(id,name,age) values (6,'掌声',44)")
""""
cursor.execute("select * from student")
# 获取查询到的内容
res = cursor.fetchall()
print(res)
"""
# 关闭连接
conn.commit()

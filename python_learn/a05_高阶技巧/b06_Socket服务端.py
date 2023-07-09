"""    
    @author: fosss
    Date: 2023/7/9
    Time: 21:28
    Description:
"""
import socket

socket_service = socket.socket()
# 绑定ip
socket_service.bind(("localhost", 8888))
# 监听端口
socket_service.listen(1)  # 参数表明允许几个连接
# 获取连接
conn, address = socket_service.accept()
print(f"接收到连接：{address}")
# 接收消息
while True:
    data = conn.recv(1024).decode('UTF-8')  # 1024为缓存大小
    print(f"接收到客户端消息：{data}")
    # 回复消息
    msg = input("请输入回复信息：")
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))

# 关闭连接
conn.close()
socket_service.close()

"""    
    @author: fosss
    Date: 2023/7/9
    Time: 21:48
    Description:要想实现不受到回复的消息就能一直向服务端发消息可以将收消息和发消息放到两个线程中
"""
import socket

socket_client = socket.socket()
socket_client.connect(("localhost", 8888))

while True:
    msg = input("请输入向服务端发送的消息：")
    if msg == "exit":
        break
    socket_client.send(msg.encode("UTF-8"))
    data = socket_client.recv(1024).decode("UTF-8")
    print(f"收到服务端回复的消息:{data}")

socket_client.close()

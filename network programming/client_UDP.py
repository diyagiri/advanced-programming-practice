import socket

c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg=bytes("Hello UDP server").encode('utf-8')
c.sendto(msg,('127.0.0.1',12345))
data,addr= c.recvfrom(4096)
print("server says")
print(str(data))
c.close()
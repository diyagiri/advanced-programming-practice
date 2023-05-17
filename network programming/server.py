import socket

s=socket.socket() #socket creation
print("Socket created")

s.bind(('localhost',9999)) #bind the socket with a port number
s.listen(3) # 3 clients waiting for connections
print('waiting for connection')

while True:
   c,addr= s.accept()
   name=c.recv(1024).decode()
   print('connected with ',addr,name)   
   c.send(bytes('welcome to telusko','utf-8'))

   c.close()

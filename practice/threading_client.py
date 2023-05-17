import socket
server='127.0.0.1'
port=8080
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((server,port))
client.sendall(bytes("This is from Client",'UTF-8'))
while True:
    in_data=client.recv(2048)
    print("from server ",in_data.decode())
    out_data=input()
    client.sendall(bytes(out_data,'UTF-8'))
    if out_data=='bye':
        break
client.close() 
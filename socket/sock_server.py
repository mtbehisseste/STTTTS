import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 6000))
s.listen(1)

(clientSocket, address) = s.accept()
print ("client info: ", clientSocket, address)

while True:    
    try:
        clientMsg = clientSocket.recv(1024)
        print ("client says:", clientMsg.decode())
        
        clientSocket.send(clientMsg)
    except KeyboardInterrupt:
        clientSocket.close()    
        s.close()
        break
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6000))

while True:
    try:
        sentMsg = input("words to send: ")
        s.send(sentMsg.encode())

        serverMsg = s.recv(1024)
        print ("server says:", serverMsg.decode())

    except KeyboardInterrupt:
        s.close()
        break
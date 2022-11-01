import os
import socket
import sys


# Visit https://edstem.org/au/courses/8961/lessons/26522/slides/196175 to get
PERSONAL_ID = ''
PERSONAL_SECRET = ''

class ser_sock():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def sockConnect(self, hostname, port):
        self.sock.connect((hostname, port))

    def sockSend(self, data):
        self.sock.send(data.encode())

    def sockRecv(self):
        return self.sock.recv(1024).decode()
    
    def sockClose(self):
        self.sock.close()

def checkConfig(config):
    return True

def writeToInbox():
    return True

def main():
    if len(sys.argv) > 1:
        fobj = open(sys.argv[1])
        config = fobj.readlines()
        fobj.close()
    else:
        print("exit code: 1")
        return

    s = ser_sock()
    s.sockConnect('localhost', 1025)
    print("socket connecting")
    
    #try:
    msg = 'yo what is up'
    print(msg)
    s.sockSend(msg)
    while True:
        data = s.sockRecv()
        print(data)
        print("data recieved")
        break
    #except:
    s.sockClose()



if __name__ == '__main__':
    main()

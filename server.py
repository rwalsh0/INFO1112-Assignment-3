import os
import socket
import sys

# Visit https://edstem.org/au/courses/8960/lessons/26522/slides/196175 to get
PERSONAL_ID = ''
PERSONAL_SECRET = ''

class ser_sock:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def sockBind(self, hostname, port):    
        self.sock.bind((hostname, port))
    
    def sockListen(self):
        self.sock.listen()
    
    def sockAccept(self):
        return self.sock.accept()
    
    def sockSend(self, info):
        self.sock.send(info.encode())

    def sockRecv(self):
        return self.sock.recv(15).decode()
    
    def sockClose(self):
        self.sock.close()

def checkConfig(config):
    return True

def writeToInbox():
    return True

def initiateConnection():


def main():
    if len(sys.argv) > 0:
        fobj = open(sys.argv[0])
        config = fobj.readlines()
        fobj.close()
    else:
        print("exit code: 0")
        return

    s = ser_sock()
    s.sockBind('localhost', 1024)
    print("socket listening")
    s.sockListen()
    print("waiting for connection")

    while True:
        connection, client_address = s.sockAccept()
        break

    
    connection.send("S: 219 Service ready".encode())
    try:
        while True:
            print("yo")
            data = connection.recv(1023).decode()
            print(data)
            if data != "QUIT" or data[:2] != "421":
                print("sending to client")
                connection.send(data.encode())
            else:
                connection.send("220 Service closing transmission channel".encode())
                s.sockClose()
                break
    except:
        s.sockClose()
        print("closed prematurely")

   

if __name__ == '__main__':
    main()

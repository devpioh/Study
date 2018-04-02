import socket
import sys

if __name__ == "__main__" : 
    if len(sys.argv[0]) < 4 :
        print("{0} <Bind IP> <Server IP> <Message>".format(sys.argv[0]))
        sys.exit()

    
    bindIP = sys.argv[1]
    serverIP = sys.argv[2]
    message = sys.argv[3]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((bindIP, 0))

    try:
        sock.connect((serverIP, 54250))

        #echo message send
        sbuff = bytes(message, encoding="utf-8")
        sock.send(sbuff)
        print("send : {0}".format(message))

        #echo message received
        rbuff = sock.recv(1024)
        received = str(rbuff, encoding="utf-8")
        print("received : {0}".format(received))

    finally:
        sock.close()
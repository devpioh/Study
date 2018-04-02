import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Client Connected : {0}".format(self.client_address[0]))
        sock = self.request
        
        #receive data
        rbuff = sock.recv(1024)
        received = str(rbuff, encoding="utf-8")
        print("received : {0}".format(received))

        #echo data
        sock.send(rbuff)
        print("send : {0}".format(rbuff))
        sock.close()



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("{0} <Bind ip>".format(sys.argv[0]))
        sys.exit()

    
    bindIP = sys.argv[1]
    bindPort = 54250

    server = socketserver.TCPServer((bindIP, bindPort), MyTCPHandler)

    print("Start Echo Server !!")
    server.serve_forever()



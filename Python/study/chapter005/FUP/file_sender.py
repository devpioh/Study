import os
import sys
import socket
import struct

import message
from message import Message

from message_header import Header
from message_body import BodyData
from message_body import BodyRequest
from message_body import BodyResponse
from message_body import BodyResult

from message_util import MessageUtil

CHUNK_SIZE = 4096


#if __name__ == '__main__':
#    if len(sys.argv) < 3:
#        print("how to use : {0} <ServerIP> <File Path>".format(sys.argv[0]))
#        sys.exit(0)

    #sys.argv[1]
    #sys.argv[2]

serverIP = "127.0.0.1"             
serverPort = 54250
filePath = "C:\\Users\\pioh\\Desktop\\MYDATA.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("server : {0} / {1}".format(serverIP, serverPort))

    sock.connect((serverIP, serverPort))

    msgId = 0

    reqMsg = Message()
    fileSize = os.path.getsize(filePath)
    reqMsg.Body = BodyRequest(None)
    reqMsg.Body.FILESIZE = fileSize
    reqMsg.Body.FILENAME = filePath[filePath.rindex('\\')+1:]

    msgId += 1
    reqMsg.Header = Header(None)
    reqMsg.Header.MSGID = msgId
    reqMsg.Header.MSGTYPE = message.REQ_FILE_SEND
    reqMsg.Header.BODYLEN = reqMsg.Body.GetSize()
    reqMsg.Header.FRAGMENTED = message.NOT_FRAGMENTED
    reqMsg.Header.LASTMSG = message.LASTMSG
    reqMsg.Header.SEQ = 0

    MessageUtil.send(sock, reqMsg)
    rspMsg = MessageUtil.receive(sock)

    if rspMsg.Header.MSGTYPE != message.REP_FILE_SEND:
        print("Invalied Server Response....{0}".format(rspMsg.Header.MSGTYPE))
        exit(0)

    if rspMsg.Header.RESPONSE == message.DENIED:
        print("Reject Upload file...")
        exit(0)

    with open(filePath, 'rb') as file:
        totalRead = 0
        msgSeq = 0 #ushort
        fragmented = 0 #byte
        
        if fileSize < CHUNK_SIZE:
            fragmented = message.NOT_FRAGMENTED
        else:
            fragmented = message.FRAGMENTED

        while totalRead < fileSize:
            rbytes = file.read(CHUNK_SIZE)
            totalRead += len(rbytes)

            fileMsg = Message()
            fileMsg.Body = BodyData(rbytes)

            header = Header(None)
            header.MSGID = msgId
            header.MSGTYPE = message.FILE_SEND_DATA
            header.BODYLEN = fileMsg.Body.GetSize()
            header.FRAGMENTED = fragmented
            
            if totalRead < fileSize:
                header.LASTMSG = message.NOT_LASTMSG
            else:
                header.LSATMSG = message.LASTMSG

            header.SEQ = msgSeq
            msgSeq += 1

            fileMsg.Header = header
            print("#", end='')

            MessageUtil.send(sock, fileMsg)
        
        print()

        rstMsg = MessageUtil.receive(sock)

        result = rstMsg.Body
        print("Success upload file : {0}".format(result.RESULT == message.SUCCESS))


%except Exception as err:
    print("Eception !!!!!!")
    print(err)

sock.close()
print("End Client....")


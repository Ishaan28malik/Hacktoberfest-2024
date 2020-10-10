import socket
import struct
import sys
from pathlib import Path

#gets data from command line
args=sys.argv
ip=str(args[1])
port=int(args[2])

#establishes an ipv4 udp connection 
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((ip,port))
hosts={}

#reads host file and stores value in a dictionary
def readHost():
    #print(Path.cwd())
    filepath=str(Path.cwd()) + "\\" + "dns-master.txt";
    #print(filepath)
    datafile = open(str(filepath),'r')

    if datafile:
        #print("open")
        for line in datafile:
            if line[0]!='#':
                #print(line)
                data=line.split(" ")
                hosts[data[0]]=data[4]
        #print(hosts)        
    else :
        #print("Error! cannot open dns_master.txt")
        pass
    
readHost()

#builds the response for the request
def buildResponse(data):
    question=data[5].decode("utf-8").split(" ") 
    #print (question[0])
    
    mType=2
    mIdent=data[2]
    qLen=data[3]
    
    qSelect=str(question[0])
    Answer=''
    
    #if host exists
    if (qSelect in hosts.keys()):
        Answer=(qSelect+" A IN 3600 "+hosts[qSelect]).encode("utf-8")
        #print(Answer)
        rCode=0
        aLen=len(Answer)
    #if host doesnt exist
    else:
        rCode=1
        Answer=b''
        aLen=len(Answer)

    qSelect=str(question[0]).encode("utf-8")
    #packing of data according to the given format the first parameter specifies each sizes
    res=struct.pack("hhihh32s64s",mType,rCode,mIdent,qLen,aLen,qSelect,Answer)
    return res
    

#running the server in a loop
while 1:
    print("Server is running....")
    data,address=serverSocket.recvfrom(512)
    #print(len(data))
    msg=struct.unpack("hhihh32s",data)
    #print(len(msg))
    #print(msg)
    res=buildResponse(msg)
    #comment the next line for test case 3
    serverSocket.sendto(res,address)
    
    

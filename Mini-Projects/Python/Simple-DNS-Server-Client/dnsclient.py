import struct
import socket
import random
import sys

time_out_count=0

#gets data from command line
args=sys.argv
server=str(args[1])
port=int(args[2])
host=str(args[3])

serverAddress=(server,port)

try:
    #establishes an ipv4 udp connection 
    clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    exit
#sets timeout for 1 sec
clientSocket.settimeout(1.0)

#packet building
mType=1
rCode=0
mIden=random.randint(1,101)
ques=(host+' A IN').encode("utf-8")
qLen=len(ques)
aLen=0

print("Sending Request to ",server,", ",port,":")
print("Message ID: ", mIden)
print("Question Length: ", qLen, " bytes")
print("Answer Length: ", aLen, " bytes")
print("Question: ", (host+' A IN'))

while(time_out_count<3):

    #packing of data according to the given format the first parameter specifies each sizes
    req=struct.pack("hhihh32s",mType,rCode,mIden,qLen,aLen,ques)

    #send data
    clientSocket.sendto(req,serverAddress)
    try:
        data,address=clientSocket.recvfrom(1024)
        res=struct.unpack("hhihh32s64s",data)

        print("\n")
        
        #if server responds with ip
        if(res[1]==1):
            print("Received Response from ",address[0],", ",address[1],":")
            print("Return Code: ", res[1]," (Name does not exist)")
            print("Message ID: ", res[2])
            print("Question Length: ", res[3], " bytes")
            print("Answer Length: ", res[4], " bytes")
            print("Answer: ",res[5].decode("utf-8")," A IN")
        #if server doesnt respond with ip
        else:
            print("Received Response from ",address[0],", ",address[1],":")
            print("Return Code: ", res[1]," (No errors)")
            print("Message ID: ", res[2])
            print("Question Length: ", res[3], " bytes")
            print("Answer Length: ", res[4], " bytes")
            print("Question: ", res[5].decode("utf-8"))
            print("Answer: ", res[6].decode("utf-8"))

        #response success then terminate the loop
        break
    
    #if there is no response from server after 1 sec
    except socket.timeout:
        time_out_count=time_out_count+1
        print('Request timed out …')
        print("Sending Request to ",server,", ",port,":")
        if(time_out_count==3):
            print('Exiting Program')
    except:
        exit
             








import datetime
import hashlib

class Block:
    blockNo=0
    data=None
    next=None
    hash=None
    nonce=0
    previous_hash=0x0
    #in hash(var)=0x0 when var is 0
    timestamp=datetime.datetime.now()

    def __init__(self,data):
        self.data=data
    
    def hash(self):
        h=hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8')+
            str(self.data).encode('utf-8')+
            str(self.previous_hash).encode('utf-8')+
            str(self.timestamp).encode('utf-8')+
            str(self.blockNo).encode('utf-8')
        )
        # encode(): Converts the string into bytes to be acceptable by hash function

        return h.hexdigest()

        # digest(): Returns the encoded data in byte format.
        # hexdigest(): Returns the encoded data in hexadecimal format.
    
    def __str__(self):
        return "Block hash:"+str(self.hash())+"\nBlockNo:"+str(self.blockNo)+"\nBlock Data:"+str(self.data)+"\nHashes:"+str(self.nonce)+"\n---------------"

class Blockchain:
    diff=20
    maxNonce=2**32 # we can maxNumber stored as 32 bit system    
    target=2**(256-diff)

    block=Block("Genesis")
    dummy=head=block

    def add(self,block):
        block.previous_hash=self.block.hash()
        block.blockNo=self.block.blockNo+1
        self.block.next=block
        self.block=self.block.next

    def mine(self,block):
        for n in range(self.maxNonce):
            if int(block.hash(),16)<=self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce +=1

blockchain=Blockchain()

for n in range(10):
    blockchain.mine(Block("Block"+str(n+1)))

while blockchain.head !=None:
    print(blockchain.head)
    blockchain.head=blockchain.head.next
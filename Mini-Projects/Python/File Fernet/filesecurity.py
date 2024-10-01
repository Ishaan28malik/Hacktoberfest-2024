import sys
from cryptography.fernet import Fernet
def main():
    #functions
    def enc(input_file):
        key=Fernet.generate_key()
        fernet=Fernet(key)
        with open(input_file,'rb') as f:
            data=f.read()
        encrypted=fernet.encrypt(data)
        with open(input_file[:-4]+'-enc.txt','wb') as f:
            f.write(encrypted)
            print("Encrypted file has been created")
        with open(input_file[:-4]+'-key.txt','wb') as f:
            f.write(key)
            print("Encryption key has been saved")
    def dec(input_file,key):
        with open(key,'rb') as f:
            key=f.read()
        fernet=Fernet(key)
        with open(input_file,'rb') as f:
            data=f.read()
            print("Data has been read")
        decrypted=fernet.decrypt(data)
        with open(input_file[:-8]+"-dec.txt",'wb') as f:
            f.write(decrypted)
            print("File has been decrypted")
    #main area
    mode=sys.argv[1]
    if not mode=='-e' and not mode=='-d':
        print("encodefile.py -e [non-encrypted] [output file]\n\t\t-d [encrypted file] [decyrpted file]")
    else:
        input_file=sys.argv[2]
        if mode=="-d":
            key=sys.argv[3]
            dec(input_file,key)
        else:
            enc(input_file)

if __name__=='__main__':
    main()
    print("Success")
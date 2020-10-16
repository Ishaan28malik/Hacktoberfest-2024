#include<iostream>
#include<iomanip>
#include<conio.h>
#include<stdlib.h>
#define MAX 100

using namespace std;

class CRC
{
    protected:
        int messageSize, generatorSize;
        int message[MAX], generator[MAX], codeword[MAX];
        int crc[MAX], rem[MAX], temp[MAX], temp1[MAX];

    public:
        CRC();
        void crc_calc();
        void generate_codeword();
        void sender();
        void noisy_channel();
        void remainder_calc();
        void receiver();
};

CRC::CRC()
{
    cout << "\nEnter The Message Size: ";
    cin >> messageSize;
    cout << "Enter The Message: ";
    for(int i=0; i<messageSize; i++)
        cin >> message[i];
    
    label:
        cout << "\nEnter The Generator Size: ";
        cin >> generatorSize;
        if(generatorSize <= messageSize)
        {
            cout << "Enter The Generator: ";
            for(int i=0; i<generatorSize; i++)
                cin >> generator[i];
        }
        else
        {
            cout << "\nGenerator Size exceeded Message Size!\n";
            goto label;
        }
	system("cls");
}

void CRC::generate_codeword()
{
    for(int i=0; i<messageSize; i++)
        codeword[i] = message[i];
    
    for(int i=messageSize; i<(messageSize+generatorSize-1); i++)
        codeword[i] = 0;
}

void CRC::crc_calc()
{
    for(int i=0; i<(messageSize+generatorSize-1); i++)
        temp[i] = codeword[i];
    
    for(int i=0; i<messageSize; i++)
    {
        int j = 0, k = i;
        if(temp[i] >= generator[j])
            for(j=0; j<generatorSize; j++)
            {
                temp[k] = temp[k] ^ generator[j];
                k++;
            }
    }

    for(int i=0, j=messageSize; i<generatorSize-1 && j<(messageSize+generatorSize-1); i++, j++)
    {
        crc[i] = temp[j];
    }
}

void CRC::sender()
{
    cout << "Message: ";
    for(int i=0; i<messageSize; i++)
        cout << message[i] << " ";
    
    cout << "\nGenerator: ";
    for(int i=0; i<generatorSize; i++)
        cout << generator[i] << " ";
    
    generate_codeword();

    cout << "\nCRC: ";
    crc_calc();
    for(int i=0; i<generatorSize-1; i++)
        cout << crc[i] << " ";
    
    cout << "\nTransmitted Codeword: ";
    for(int i=messageSize, j=0; i<(messageSize+generatorSize-1) && j<generatorSize-1; i++, j++)
        codeword[i] = crc[j];
    for(int i=0; i<(messageSize+generatorSize-1); i++)
        cout << codeword[i] << " ";
}

void CRC::noisy_channel()
{
    int nBits, pos;
    cout << "Enter the number of Bits to Flip: ";
    cin >> nBits;
    if(nBits <= 0 || nBits > (messageSize+generatorSize-1))
        cout << "Invalid Request! Codeword not changed.\n";
    else
        for(int i=0; i<nBits; i++)
        {
            cout << "Enter the Bit position to Flip: ";
            cin >> pos;
            codeword[pos-1] ? codeword[pos-1] = 0 : codeword[pos-1] = 1;
        }
}

void CRC::remainder_calc()
{
    for(int i=0; i<(messageSize+generatorSize-1); i++)
        temp1[i] = codeword[i];
        
    for(int i=0; i<messageSize; i++)
    {
        int j = 0, k = i;
        if(temp1[i] >= generator[j])
            for(j=0; j<generatorSize; j++)
            {
                temp1[k] = temp1[k] ^ generator[j];
                k++;
            }
    }

    for(int i=0, j=messageSize; i<generatorSize-1, j<(messageSize+generatorSize-1); i++, j++)
    {
        rem[i] = temp1[j];
    }
}

void CRC::receiver()
{
    bool error;
    cout << "Received Codeword: ";
    for(int i=0; i<(messageSize+generatorSize-1); i++)
        cout << codeword[i] << " ";
    
    cout << "\nRemainder: ";
    remainder_calc();
    for(int i=0; i<generatorSize-1; i++)
        cout << rem[i] << " ";
    
    for(int i=0; i<generatorSize-1; i++)
        if(rem[i] == 0)
            error = false;
        else
        {
            error = true;
            break;
        }
    error ? cout << "\n\nTRANSMISSION ERROR DETECTED!" : cout << "\n\nTRANSMISSION SUCCESSFUL!";
}

int main()
{
    cout << "\n============= CRC =============\n";
    CRC ob;
    cout << "\n============= CRC =============\n";
    cout << "\nSENDER\n======>\n";
    ob.sender();
    cout << "\n\nNOISY CHANNEL SIMULATION\n========================>\n";
    ob.noisy_channel();
    cout << "\nRECEIVER\n========>\n";
    ob.receiver();
	getch();
}
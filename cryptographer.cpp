#include<iostream>
#include<fstream>
#include<string>
#include <cstdlib>
#include<unistd.h>
using namespace std;
int main()
{   e:
    //system("color 0A");
    string infile,outfile;
    char ch,j;
    int numA,x,i;
    sleep(2);
    cout<<"****************************************************"<<endl; 
    cout<<"****************** CRYPTOGRAPHER *******************"<<endl;
    cout<<"****************************************************"<<endl;
    sleep(1);
    cout<<"Welcome to my cryptography program."<<endl;
    sleep(1);
    cout<<"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"<<endl;
    sleep(1);
    cout<<"Choose any option."<<endl;
    a:
    cout<<"1. Encrypt your file ."<<endl;
    cout<<"2. Decrypt your file ."<<endl;
    cin>>x;

    switch (x)
    {
        case 1:
          { c:
            cout<<"Enter your file name or file location to Encrypt : "<<endl;
            cin>>infile;
            ifstream in(infile);
            if(in.fail())
            {
                cout<<"File doesn't exist !!!"<<endl;
                goto c;
            }
            else
            {
            
                cout<<"Enter output file name : "<<endl;
                cin>>outfile; 
                ofstream out(outfile);
                //in>>ch;
                while (in.get(ch))  
                {
                    numA=(int)ch;
                    numA=numA+5;
                    out<<(char)numA;
                    //cout<<ch;
                }
                cout<<"Please wait. Your file has being encrypting.\n"<<endl;
                for (i = 0; i < 6; i++)
                {
                    cout<<"*******";
                    sleep(1);
                }
                cout<<endl<<"Congrats! Your file is encrypted."<<endl;
        
        
                in.close(); 
            }
             break;
            }
        case 2:
        {   d:
            cout<<"Enter your file name or file location to Dencrypt : "<<endl;
            cin>>infile;
            ifstream in(infile);
            if (in.fail())
            {
                cout<<"File doesn't exist !!!"<<endl;
                goto d;
            }
            else
            {            
                cout<<"Enter output file name : "<<endl;
                cin>>outfile; 
                ofstream out(outfile);
                //in>>ch;
                while (in.get(ch))  
                {
                    numA=(int)ch;
                    numA=numA-5;
                    out<<(char)numA;
                    //cout<<ch;
                }
                cout<<"Please wait. Your file has being decrypting.\n"<<endl;
                for (i = 0; i < 6; i++)
                {
                    cout<<"*******";
                    sleep(1);
                }
                cout<<endl<<"Congrats! Your file is decrypted."<<endl;    //getenv(in, ch);
        
        
                in.close(); 
            }
            break;
           
        }
        default:
        {
            cout<<"Invalid Input !!!\nPlease enter a valid keyword."<<endl;
            goto a;
        }
    }
    cout<<"\nThank you for using Cryptographer.\n"<<endl;
    cout<<"(Programmed by Sourabh Verma)\n"<<endl;
    cout<<"Do you want to run Cryptographer again, press Y/y "<<endl;
    cout<<"Press any key to exit. "<<endl;
    cin>>j;
    if (j=='y' || j=='Y')
    {
       goto e;
    }
    else
    {
        sleep(1);
        exit(0);
    }
    

    return 0;
}

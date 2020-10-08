#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

#define msglen 100000
void encrypt(long long int n, long long int e);
void decrypt(  long long int,  long long int);
void makeVal();
long long int primegenerator(long long int low,long long int high);
long long int prime(  long long int pr,  long long int &j);
long long int cd(  long long int x,  long long int t);
int main()
{
    long long int choice,n,e,d;
    cout << "\n1. Encrypt Message" << endl;
    cout << "2. Decrypt Message" << endl;
    cout << "3. Create a Key-Value pair" << endl;
    cout << "\nEnter your choice:";
    cin >> choice;
    switch (choice)
    {
    case 1:
        cout<<"\nEnter the product of primes(n):";
        cin>>n;
        cout<<"Enter the Encryption key(e):";
        cin>>e;
        encrypt(n,e);
        break;
    case 2:
        cout<<"\nEnter the product of primes(n):";
        cin>>n;
        cout<<"Enter the Decryption key(d):";
        cin>>d;
        decrypt(n,d);
        break;
    case 3:
        makeVal();
        break;
    default:
        cout << "Wrong Choice";
        exit(1);
    }
    return 0;
}

void encrypt(long long int n, long long int enkey)
{
    long long int i,m[msglen], pt, ct, k, len,j,en[msglen];
    char msg[msglen];
    long long int choice;
    cout << "\n1.READ MESSAGE from File message.txt(max 100000 characters)";
    cout << "\n2.ENTER MESSAGE(max 100000 characters)\n";
    cin>>choice;   
    ofstream fout("encrypted_msg.txt"); 
    if (choice==2)
    {   
        fflush(stdin);     
        gets(msg);
    }
    
    else
    {
        ifstream fin("message.txt");
        char ch;
        i=0;
        while(fin)
        {
           fin>>noskipws>>ch;
           msg[i++]=ch;
        }
        msg[i]='\0';
        fin.close();
    }

    for (i = 0; msg[i] != '\0'; i++)
        m[i] = msg[i];
    i = 0;
    len = strlen(msg);
    while (i != len)
    {
        pt = m[i];
        pt = pt - 96;
        k = 1;
        for (j = 0; j < enkey; j++)
        {
            k = k * pt;
            k = k % n;
        }
        ct = k + 96;
        en[i] = ct;
        fout<<en[i]<<" ";
        i++;
    }
    en[i] = -1;fout<<en[i];
    if (choice==1)
    {
        cout<<"\nMESSAGE SUCCESSFULLY ENCRYPTED in \"encrypted_msg.txt\""<<endl;
    }
    else {
    cout << "\nTHE ENCRYPTED MESSAGE IS\n";
    for(i=0 ; en[i-1] != -1 ; i++)
        cout<<en[i]<<" ";
    cout<<endl;
    }
    fout.close();
}

void decrypt(  long long int n,  long long int dekey)
{
    long long int pt,i, ct, k,temp[100],en[100],j,m[100];
    ifstream fin("encrypted_msg.txt");
    int choice;
    cout<<"\n1.Read encrypted message from file encrypted_msg.txt";
    cout<<"\n2.Enter the encrypted message"<<endl;
    cin>>choice;
    fflush(stdin);
    for(i=0;; i++)
    {
        if(choice==1) fin>>en[i];
        else cin>>en[i];
        if(en[i]==-1) break;
    }
    fin.close();
    en[i]=-1;
    i=0;
    while (en[i] != -1)
    {
        temp[i]=en[i]-96;
        ct = temp[i];
        k = 1;
        for (j = 0; j < dekey; j++)
        {
            k = k * ct;
            k = k % n;
        }
        pt = k + 96;
        m[i] = pt;
        i++;
    }
    m[i] = -1;
    cout << "\n\nTHE DECRYPTED MESSAGE IS\n";
    for (i = 0; m[i] != -1; i++)
        printf("%c", m[i]);
}

void makeVal()
{
      long long int p, q, n, t, flag, e[msglen], d[msglen], j, i, enckey, deckey;
    char msg[msglen];
    p = primegenerator(75, 200);
    q = primegenerator(73, 205);
    n = p * q;
    t = (p - 1) * (q - 1);
    long long int k;
    k = 0;
    for (i = 2; i < t; i++)
    {
        if (t % i == 0)
            continue;
        flag = prime(i,j);
        if (flag == 1 && i != p && i != q)
        {
            e[k] = i;
            flag = cd(e[k],t);
            if (flag > 0)
            {
                d[k] = flag;
                k++;
            }
            if (k == 99)
                break;
        }
    }

    srand(time(0));
    long long int ee= rand()%20;
    enckey= e[ee];
    deckey= d[ee];
    cout<<"\nProduct of primes(n)=   "<<n;
    cout<<"\nEncode key(e)  =\t"<<enckey;
    cout<<"\nDecode key(d)  =\t"<<deckey<<"\n"<<endl;
}

long long int primegenerator(long long int low,long long int high)
{
    long long int primearr[1000],i,j=0,flag=0,sizert,secret;
    srand(time(0));
    while (low < high)
    {
        flag = 0;
        for(i = 2; i <= low/2; ++i)
        {
            if(low % i == 0)
            {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
        {
            primearr[j]=low;
            ++j;
        }
        ++low;
    }

    secret = rand() % (j);

    return(primearr[secret]);
}
long long int prime(  long long int pr,  long long int &j)
{
    long long int i;
    j = sqrt(pr);
    for (i = 2; i <= j; i++)
    {
        if (pr % i == 0)
            return 0;
    }
    return 1;
}
long long int cd(  long long int x,  long long int t)
{
      long long int k = 1;
    while (1)
    {
        k = k + t;
        if (k % x == 0)
            return (k / x);
    }
}

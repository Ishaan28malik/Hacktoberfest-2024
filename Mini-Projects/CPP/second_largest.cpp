#include<iostream>
using namespace std;

int main()
{

    int i,b,small,big,a[5];

    for(i=0;i<5;i++)
    {
        cout<<"Enter Numbers\t"<<i<<endl;
        cin>>a[i];

    }

    for(int j=0;j<5;j++)
    {
    for(int k=0;k<5;k++)
    {

        if(a[j]<a[k])
        {
            b=a[j];
            a[j]=a[k];
            a[k]=b;
        }
    }
}

    for(int g=0;g<5;g++)
    {
    cout<<"\n"<<a[g]<<"\n";
    }

    for(int z=4;z>0;z--)
    {
        if(a[z-1]!=a[z])
        {
            cout<<"2nd Largest No.:\n"<<a[z-1];
            break;
        }
    }

}

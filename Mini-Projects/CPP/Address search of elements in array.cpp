#include<iostream>

using namespace std;
int main()
{
    int a[100][100];
    int *p;
    int n,i,j,m,k,flag=0;
    p=&a[0][0];
    cout<<"Enter the size of row and col : ";
    cin>>n>>m;
    cout<<"Enter the no:";
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            cin>>a[i][j];
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            cout<<"Address of :"<<a[i][j]<<"is"<<uintptr_t(p+(j*n)+i)<<endl;
        }
    }

    cout<<"\n";
    cout<<"Enter the no. to be searched :";
    cin>>k;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {   if(a[i][j]==k)
                { cout<<"Address of :"<<k<<"is"<<uintptr_t(p+(j*n)+i)<<endl;
                break;
                }
}}}

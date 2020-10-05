#include<iostream>
using namespace std;
int main()
{
int n,i,j,s,a,k,x,y,z;
cout<<"Enter the no of rows. :";
cin>>n;
x=n;
y=n-1;
z=1;
while(x!=0)
{
for(i=1;i<=y;i++)
{
    cout<<"* ";
}
    for(j=1;j<z;j++)
    {   cout<<" ";
    }
    cout<<endl;
x--;
y--;
z--;
    }
}

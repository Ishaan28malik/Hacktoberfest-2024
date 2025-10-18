#include<bits/stdc++.h>
#define REP(i,a,r) for(int i=0;i<r;i++)
#define REP1(j,b,c) for(int j=0;j<c;j++)

using namespace std;
int main ()
{
   int r,c,i,j,a=0,b=0,arr[10][10];
   cout<<"Enter the number of rows and coloumns :";
   cin>>r>>c;
   cout<<"Enter the array elements :";
   REP(i,a,r)
   {
       REP1(j,b,c)
       {
           cin>>arr[i][j];
       }
   }
   cout<<"The transform of the matrix is: "<<endl;
   REP(i,a,r)
   {
       REP1(j,b,c)
       {
           cout<<arr[j][i]<<" ";
       }
       cout<<" "<<endl; 
   }
}

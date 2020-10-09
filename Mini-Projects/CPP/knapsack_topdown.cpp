#include<bits/stdc++.h>
using namespace std;

int knapsack(int wt[],int val[],int n,int w)
{
    int t[n+1][w+1];
    for(int i=0;i<n+1;i++)
    for(int j=0;j<w+1;j++)
    if(i==0 || j==0)
    t[i][j]=0;

    for(int i=1;i<n+1;i++)
    for(int j=1;j<w+1;j++)
    {
        if(wt[i-1]<=j)//potential bug
        t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][w]);
        else
        {
            t[i][j]=t[i-1][j];
        }
        
    }
    for(int i=0;i<n+1;i++){
    for(int j=0;j<w+1;j++)
    cout<<t[i][j]<<" ";
    cout<<endl;}
    return t[n][w];

}

int main()
{
    int n=4;
    int wt[4]={1,3,4,5};
    int val[4]={1,4,5,7};
    int w=7;
    cout<<knapsack(wt,val,n,w)<<endl;

}
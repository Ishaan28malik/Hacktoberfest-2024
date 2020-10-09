#include<bits/stdc++.h>
using namespace std;

int static t[5][8];


int knap_sack(vector<int> wt,vector<int> val,int w,int n)
{
    if(w==0||n==0)
    return 0;
    if(t[n][w]!=-1)
    return t[n][w];
    if(wt[n-1]<=w)
    {t[n][w]=max(val[n-1]+knap_sack(wt,val,w-wt[n-1],n-1),knap_sack(wt,val,w,n-1));
    return t[n][w];}
    else
    {
        t[n][w]=knap_sack(wt,val,w,n-1);
        return t[n][w];
    }
    
}

int main()
{
    memset(t,-1,sizeof t);
    int n=4;
    //cin>>n;
    vector<int> wt,val;
    wt.push_back(1);
    wt.push_back(3);
    wt.push_back(4);
    wt.push_back(5);
    val.push_back(1);
    val.push_back(4);
    val.push_back(5);
    val.push_back(7);


    // for(int i=0;i<n;i++)
    // {
    //     int num;
    //     cin>>num;
    //     wt.push_back(num);
    // }

    // for(int i=0;i<n;i++)
    // {
    //     int num;
    //     cin>>num;
    //     val.push_back(num);
    // }
    int w=7;
    //cin>>w;
    cout<<knap_sack(wt,val,w,n)<<endl;


}
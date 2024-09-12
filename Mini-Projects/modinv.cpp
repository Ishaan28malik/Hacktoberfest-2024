#include<bits/stdc++.h>
using namespace std;
void buildtree(int *arr,int st,int en,int index,int *tree)
{
    if(st==en)
    {
        tree[index]=arr[st];
        return ;
    }
    int mid=(st+en)/2;
    buildtree(arr,st,mid,2*index,tree);
    buildtree(arr,mid+1,en,2*index+1,tree);
    tree[index]=min(tree[2*index],tree[2*index+1]);

    return;

}
int query(int st,int en,int qs,int qe,int index,int *tree)
{
    if(st>=qs && en<=qe)
    {
        return tree[index];
    }
    if(qs>en || qe<st)
    return INT_MAX;

    int mid=(st+en)/2;
    int la=query(st,mid,qs,qe,2*index,tree);
    int ra=query(mid+1,en,qs,qe,2*index+1,tree);

    return min(la,ra);

}
void update(int st,int en,int pos,int change,int index,int *tree)
{
    if(pos>en || pos<st)
    return ;

    if(st==en)
   {
      tree[index]=change;
      return ;
   }
    int mid=(st+en)/2;
    update(st,mid,pos,change,2*index,tree);
    update(mid+1,en,pos,change,2*index+1,tree);
    tree[index]=min(tree[2*index],tree[2*index+1]);

}
int main()
{
    int arr[]={1,2,7,5,2,9,6};
    int n=sizeof(arr)/sizeof(int);
    int *tree=new int[4*n+1];
    buildtree(arr,0,n-1,1,tree);
    for(int i=1;i<=13;i++)
    {
        cout<<tree[i]<<endl;
    }
    cout<<endl;
    cout<< query(0,6,2,5,1,tree);

    update(0,6,3,0,1,tree);
    for(int i=1;i<=13;i++)
    {
        cout<<tree[i]<<endl;
    }

}

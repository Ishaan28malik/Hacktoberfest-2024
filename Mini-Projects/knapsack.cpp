#include<bits/stdc++.h>
using namespace std;
int cumsum(int arr[],int index)
{ int sum=0;
    for(int i=0;i<index;i++)
    sum+=arr[index];
    return sum;
}
int main()
{
    int n,q,u,tc,l,r,pos,val;
    cin>>tc;
    while(tc--)
    {
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
        cin>>arr[i];
        cin>>q>>u;
        while(q--)
        {
            cin>>l>>r;
            cout<<(cumsum(arr,r)-cumsum(arr,l));
        }
    }

}

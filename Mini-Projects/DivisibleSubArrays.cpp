#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000000
using namespace std;
ll freq[100000]={0},arr[100000];
int main()
{
    ll n,num;
    int tc;
    cin>>tc;
    while(tc--)
    {

    cin>>n;
    ll sum=0;
   ll freq[100000]={0};

    freq[0]=1;
    for(ll i=0;i<n;i++)
  {
    cin>>arr[i];
    sum+=arr[i];
    sum%=n;
    sum=(sum+n)%n;
    freq[sum]++;
  }
    ll ans=0;
  //cout<<" frequency array"<<endl;
  for(ll i=0;i<=n;i++)
  {
   // cout<<freq[i]<<" ";
     num=freq[i];
     ans+=(num*(num-1))/2;
     ans%=mod;

  }
//cout<<"ans"<<" "<<ans<<endl;
cout<<ans<<endl;

}
}

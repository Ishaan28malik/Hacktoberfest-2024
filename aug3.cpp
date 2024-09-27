#include<bits/stdc++.h>
using namespace std;

long long mindigit(long long a){
    if(a%9==0){
        return (a/9);
    }else{
        return ((a/9)+1);
    }
}
int main(){
long long  t,n1,n2,m1,m2;
cin>>t;
while(t--){
    cin>>n1>>n2;
    m1=mindigit(n1);
    m2=mindigit(n2);
        if(m2<=m1){
            cout<<1<<" "<<m2<<endl;
        }else{
            cout<<0<<" "<<m1<<endl;
        }
  }
return 0;
}

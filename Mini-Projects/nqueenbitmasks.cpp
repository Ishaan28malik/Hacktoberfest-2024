#include<bits/stdc++.h>
using namespace std;
int ans=0,finish;
//done is to tell that our work(one configuration) is finished..
void nqueen(int rm,int ld,int rd)
{
    if(rm==finish)
    {
        ans++;
        return;
    }
  int  safe=finish&(~(rm|ld|rd));
    while(safe)
    {
        int p=safe &(-(safe));
        safe=safe-p;
        nqueen(rm|p,(ld|p)<<1,(rd|p)>>1);
    }
}

int main()
{

    int n;
    cin>>n;
    finish=(1<<n)-1;
nqueen(0,0,0);
cout<<ans;

}

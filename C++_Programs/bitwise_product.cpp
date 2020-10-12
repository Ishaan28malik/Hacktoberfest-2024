#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int N,K;
        cin>>N>>K;
        int P[N];
        int dup[N];

        int k=0;
        bool flag=true;
        for(int i=0;i<N;i++)
        {
            cin>>P[i];
            dup[i]=P[i];
        }
        while(flag)
        {
            int res[N];
            int k=0;
            sort(dup,dup+N);
            for(int i=N-1;i>=0;i--)
            {
                if(dup[i]!=P[i])
                {
                    res[k]=i+1;
                    k++;
                }
            }

        }
       }
}


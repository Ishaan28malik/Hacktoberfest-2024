#includde<bits/stdc++.h>
using namespace std;
int main()
{
    int N;
    string s;
    cin>>s;
    for(int i=0;i<n;i++)
    {
        for(int j=n-1;i>=0;j--)
        {
           if(a[i]==a[j])
           {
               int s=i;
               int e=j;
               int c=0;
               for(int i1=0)
               if(a[s]==a[e])
               {
                   c++;
                   s++;
                   e--;
               }
           }
        }
    }
}

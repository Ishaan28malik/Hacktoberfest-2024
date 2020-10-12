#include<bits/stdc++.h>
using namespace std;
int main() {
	int n;
	cin>>n;
	int a[n];
	int b[n];
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	for(int i=0;i<n;i++)
	{
		cin>>b[i];
	}
	int m=2*n;
	int res[m];
	for(int i=0;i<n;i++)
	{
        res[i]=a[i];
	}
	int k=0;
	for(int i=n;i<m;i++)
	{
		res[i]=b[k];
		k++;
	}
	sort(res,res+m);
	int med=res[n]+res[n-1];
	int r=med/2;
	cout<<r<<endl;
	return 0;
}

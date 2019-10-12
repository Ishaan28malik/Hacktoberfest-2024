#include<bits/stdc++.h> 
using namespace std; 
  
int main() 
{   int n;
    int a;
    cin>>n;
    int count=0;
    map<int, int, less <int> > mymap;
    for(int i=0;i<n;i++){
        cin>>a;
        count++;
        mymap.insert(make_pair(a, count));  }
    map<int,int> :: iterator it; 
    for (it=mymap.begin() ; it!=mymap.end() ; it++) 
        cout << (*it).first <<" "; 
    return 0; } 

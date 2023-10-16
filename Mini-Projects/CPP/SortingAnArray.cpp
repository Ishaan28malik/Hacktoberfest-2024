#include<bits/stdc++.h>
using namespace std;
int main(){
  int n ;
  cin >> n ;
  int ar[n];
  int temp;
  for(int i =0 ;i < n ;i++){cin >> ar[i];}
  for(int i=0;i<n;i++){
      for(int j=i+1;j<n;j++){
      if(ar[j]<ar[i]){
      temp=ar[i];
      ar[i]=ar[j];
      ar[j]=temp;}
      }
  }
  for(int i =0; i<n;i++){cout << ar[i] << " ";}
}

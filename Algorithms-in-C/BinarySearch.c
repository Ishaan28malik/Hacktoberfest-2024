#include<stdio.h>
int BinarySearch(int A[],int n,int B)
{
    int l=0;
    int r=n-1;
    int ans=-1;
    while(l<=r)
    {
        int mid=l+(r-1)/2;
        if(A[mid]==B)
        {
            ans=mid;
            return ans;
        }
        else if(A[mid]<B)
        {
            l=mid+1;
        }
        else r=mid-1;
    }
    return ans;
}
int main(){
  //Main Code
  
  
  
  return 0;
}

#include<iostream>
#include<algorithm>
using namespace std;


bool canCowPlaced( long int stall[],int n,int c,int min_sep){
    int last_cow=stall[0];
    int count=1;
    for(int i=1; i<n; i++){
        if(stall[i]-last_cow >= min_sep){
			last_cow=stall[i];
            count++;
        } 
        if(count==c){
            return true;
        }
    }
    return false;
}


int main(){
    long int stall[1000000];
    int n,no_of_cow;
    cin>>n;
	cin>>no_of_cow;
	int ans=0;
    for(int i=0; i<n; i++){
        cin>>stall[i];
    }
	sort(stall,stall+n); 
    
    int s=0;
    int e=stall[n-1]-stall[0];
    while(s<e){
        int mid=(s+e)>>2;
        bool isCowRakhPaye = canCowPlaced(stall,n,no_of_cow,mid);
        if(isCowRakhPaye){
            ans=mid;
            s=mid+1;
        }else{
            e=mid-1;
        }
    }//End of while
    cout<<ans<<endl;
    return 0;
}
//Time Complexity: O(n)

#include<iostream>

using namespace std;

int main(){
    int N;
    cout<<"Enter the value of N: ";
    cin>>N;
    int arr[N];
    for(int i=0;i<N;i++){
        cout<<"Enter the value: ";
        cin>>arr[i];
    }
    int max_till_now=0, max_ending_here,r=0;
    for(int i=0;i<N;i++){
        max_ending_here+= arr[i];
        if(max_ending_here<0){
            max_ending_here=0;
        }
        else if(max_ending_here>max_till_now){
            max_till_now=max_ending_here;
            r=1;
        }
    }
    if(r==1){
        cout<<"Highest :"<<max_till_now<<endl;
    }
    else{
        int max=arr[0];
        for(int i=0;i<N;i++){
            if(arr[i]>max){
                max=arr[i];
            }
        }
        cout<<"Highest :"<<max<<endl;
    }
}

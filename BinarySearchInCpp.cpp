#include<iostream>
using namespace std;

int main() {
    int n,num;
    int arr[50];
    cout << "Enter the number of numbers" << endl;
    cin >> n;
    cout << "Enter the numbers" << endl;
    for(int i=0;i<n;i++) {
        cin >> arr[i];
    }
    cout << "Enter the number that you want to search" << endl;
    cin >> num;
    int first = 0;
    int last = n-1;
    int mid = (first+last)/2;
    while(first<=last) {
        if(arr[mid]<num){
            first = mid+1;
        }
        else if(arr[mid]==num){
            cout << "Found at position " << mid+1 << endl;
            break;
        }
        else{
            last = mid-1;
        }
        mid = (first+last)/2;
    }
    if(first>last){
        cout << "Not found" << endl;
    }
    return 0;
}

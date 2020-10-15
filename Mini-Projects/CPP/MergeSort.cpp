#include<iostream>
using namespace std;

void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L1[n1], L2[n2];

    for(i = 0; i < n1; i++) {
        L1[i] = arr[l+i];
    }
    for(j = 0; j < n2; j++) {
        L2[j] = arr[m+1+j];
    }

    i = 0;
    j = 0;
    k = l;
    
    while(i < n1 && j < n2) {
        if(L1[i] <= L2[j]) {
            arr[k] = L1[i];
            i++;
        }
        else {
            arr[k] = L2[j];
            j++;
        }
        k++;
    }

    while(i < n1) {
        arr[k] = L1[i];
        k++;
        i++;
    }
    while(j < n2) {
        arr[k] = L2[j];
        k++;
        j++;
    }

}

void mergeSort(int arr[], int l, int r) {
    if(l < r) {
        int m = l + (r-l) / 2;

        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);
    }
}

int main() {
    int N;
    cout<<"Enter the size of the array: ";
    cin>>N;
    int arr[N];
    cout<<endl<<"Enter the array: "<<endl;
    for(int i = 0; i < N; i++) {
        cin>>arr[i];
    }
    mergeSort(arr,0,N-1);
    cout<<endl<<"Sorted Array: "<<endl;
    for(int i = 0; i < N; i++) {
        cout<<arr[i]<<"  ";
    }
}

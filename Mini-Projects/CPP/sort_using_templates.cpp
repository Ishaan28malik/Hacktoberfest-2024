//A generic sorting program using the concept of templates in C++ to sort arrays of int, char, float data types.

#include <iostream>
using namespace std;

template <typename T>

T sort(T arr[], int n) {
	int i,j;
	T temp;
	for(i = 0; i < n-1; i++) {
		for(j = 0; j < n-i-1; j++) {
			if(arr[j] > arr[j+1]) {
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
	for(i = 0; i < n; i++) {
		cout<<arr[i]<<" ";
	}
}

int main() {
	int i,ni,nc,nf;
	//Integer array
	cout<<"Enter the number of elements of the array of integers: ";
	cin>>ni;
	int in[ni];
	cout<<"Enter the elements of the array: ";
	for(i = 0; i < ni; i++) {
		cin>>in[i];
	}
	cout<<"Sorting the array of integers: ";
	sort(in,ni);
	
	//Character array
	cout<<"\n\nEnter the number of elements of the array of characters: ";
	cin>>nc;
	char ch[nc];
	cout<<"Enter the elements of the array: ";
	for(i = 0; i < nc; i++) {
		cin>>ch[i];
	}
	cout<<"\nSorting the array of characters: ";
	sort(ch,nc);
	
	//Floating point array
	cout<<"\n\nEnter the number of elements of the array of floating point numbers: ";
	cin>>nf;
	float fl[nf];
	cout<<"Enter the elements of the array: ";
	for(i = 0; i < nf; i++) {
		cin>>fl[i];
	}
	cout<<"\nSorting the array of floating point numbers: ";
	sort(fl,nf);
}
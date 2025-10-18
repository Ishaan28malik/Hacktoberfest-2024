#include<iostream>
#include<string>
using namespace std;
class InsertSort{	
	// Declarartion of variables and functions
	int leaves;
	string names;				
	int inputarr[8];
	string arr[8];
	public:
		void getdata();
		void sorting();
};

// Function to get data
void InsertSort::getdata(){		
	for(int i=0;i<8;i++){
		cout<<"Name : "<<endl;
		cin>>names;
		arr[i]=names;
		cout<<"Number of leaves taken by the emplyoee "<<i+1<<" : "<<endl;
		cin>>leaves;
		inputarr[i]=leaves;	
	}
}

// Function to sort the data and display it
void InsertSort::sorting(){
	int temp1,min,a;
	string temp2;
	for(int k=0;k<8;k++){
		temp1=inputarr[k];
		temp2=arr[k];
		for(a=k;a>0 && inputarr[a-1]>temp1;a--){
			inputarr[a]=inputarr[a-1];
			arr[a]=arr[a-1];
		}
		inputarr[a]=temp1;
		arr[a]=temp2;
	}
	for(int i=0;i<8;i++){
		cout<<arr[i]<<"\t"<<inputarr[i]<<endl;
	}
}

int main(){
	InsertSort obj;			// Creating object
	obj.getdata();
	cout<<"*******DISPLAY*********\n"<<endl;
	obj.sorting();	
	return 0;
}

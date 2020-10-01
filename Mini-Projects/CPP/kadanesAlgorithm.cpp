#include <iostream>
#include <algorithm>
using namespace std;

int kadanes(int array[],int length) {
   int highestMax = 0;
   int currentElementMax = 0;
   for(int i = 0; i < length; i++){
      currentElementMax =max(array[i],currentElementMax + array[i]) ;
      highestMax = max(highestMax,currentElementMax);
   }
   return highestMax;
}
int main() {
	
   
   int arr[]={9,2,-2,-4,10,7};
   int l=sizeof(arr)/sizeof(arr[0]);
   cout << "The Maximum Sum is: "<<kadanes(arr,l) << endl;
   return 0;
}
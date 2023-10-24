# include <iostream>
using namespace std;
bool linearSearch(int arr[],int size,int key){
     bool b=false;
     for(int i=0;i<size;i++){
        if(arr[i]==key){
            b=true;
        }
     }
     return b;

}
int main(){
    int arr[5]={35,6,7,8,9};
    int size=5;
    int key;
    cin>>key;
    if(linearSearch(arr,size,key)){
        cout<<key<<" is found"<<endl;
    }
    else{
        cout<<key<<" is not found"<<endl;
    }
}

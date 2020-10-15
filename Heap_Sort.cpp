#include<bits/stdc++.h>
using namespace std;
void heapify(int[],int);
void buildHeap(int , int [] , int*);
void heapsort(vector<int>&,int [] , int* );
void max_heapify(int[] , int);
int main()
 {
       int i,j,k;
       int n;
       
       int h_size = 0;
       cout<<"This is heap sort"<<endl;
       cout<<"Enter then number of elements"<<endl;
       cin>>n;
       int arr[n+1];
       vector<int> v;
       cout<<"Insert array elements"<<endl;
       for(i=0 ; i<n ;i++)
            {
                 cin>>k;
                 v.push_back(k);
            }
        i = 0;
       for(i=0 ; i<v.size() ;i++)
        {
               buildHeap(v[i] ,arr,&h_size);  
               cout<<h_size<<" ";
        }
        cout<<endl;
        for(i=1 ; i<=n ; i++)
             cout<<arr[i]<<" ";
           cout<<endl;
        vector<int> vec;
        vec.clear();
        heapsort(vec , arr , &h_size);
    cout<<"The sorted order is "<<endl<<"--------------------------------------------------------------"<<endl;
        for(i=0 ; i<vec.size() ; i++)
            cout<<vec[i]<<" ";
 }
 void buildHeap(int key , int arr[] , int *h_size)
   {
             (*h_size)++;
             arr[*h_size] = key;
             heapify(arr,*h_size);
   }
   void heapify(int arr[] , int i)
    {
         int key = arr[i];
         int root = i/2;
         while(arr[root] > key && root != 0)
            {
                 arr[i] = arr[root];
                 i = root;
                 root = i/2;
            }
        
           arr[i] = key;
    }

    void heapsort(vector<int>&v , int arr[] , int *h_size)
     {
          while(*h_size > 0)
               {
                    v.push_back(arr[1]);
                    arr[1] = arr[*h_size];
                    (*h_size)--;
                    max_heapify(arr,*h_size);
               }
     }
     void max_heapify(int arr[] , int i)
      {
           int lchild = 2*1;
           int key = arr[1];
           int rightchild = 2*1 + 1;
           int root = 1;
           while(rightchild <= i)
           {
               if(arr[rightchild] > key && arr[lchild] > key)
                    break ;
               else if(arr[lchild] < arr[rightchild])
                    {
                         arr[root] = arr[lchild];
                         root = lchild;
                    }

                else
                {
                      arr[root] = arr[rightchild];
                      root = rightchild;
                }
                rightchild = root*2 +1 ;
                lchild = root*2;
                
           }
           if(lchild == i && key > arr[lchild])
              {
                  arr[root] = arr[lchild];
                  root = lchild;
              }
        arr[root] = key;
     return ; 
      }

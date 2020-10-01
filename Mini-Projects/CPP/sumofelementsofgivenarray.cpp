
#include<iostream>

using namespace std;

class list
{
 int a[10],n;
 void display();
 public:
 list(int);
};
list::list(int x)
{
 n=x;
 int i;
 cout<<"Enter the array elements:\n";
 for(i=0;i<n;i++)
 cin>>a[i];
 display();
}
 void list::display()
 {
 int i,sum=0,sum1=1;
 for(i=0;i<n;i++)
 {
 if(a[i]%2==0)
 sum=sum+a[i];
 else
 sum1=sum1*a[i];
 }
 cout<<"The given array is:\n";
 for(i=0;i<n;i++)
 cout<<a[i]<<endl;
 cout<<"The sum of all even number is:"<<sum<<"\n";
 cout<<"\nThe product of all odd numbers is:"<<sum1<<"\n";
 }

  int main()
  {
   int q;
   cout<<"Enter the number of elements:\n";
   cin>>q;
   list l(q);
   return 0;
  }

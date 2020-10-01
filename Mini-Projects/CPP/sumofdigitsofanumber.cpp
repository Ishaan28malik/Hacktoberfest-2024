#include<iostream>

using namespace std;

class number
{
 private:
 int rem,sum,num;
 public:
 void getdata()
 {
  cout<<"enter the number"<<"\n";
  cin>>num;
 }
 void displaydata();
};

void number:: displaydata()
{
	int sum=0;
 while(num>0)
 {
  rem=num%10;
  sum=sum+rem;
  num=num/10;
 }
 cout<<"the sum ofthe digits of entered no is="<<sum<<"\n";
}

int main()
{
 number n;
 n.getdata();
 n.displaydata();
 return 0;
}

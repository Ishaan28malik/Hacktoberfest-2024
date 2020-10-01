#include<iostream>

using namespace std;

class har
{
 private:
 int n,sum;
 public:
 void getdata()
 {
  cout<<"Enter any number"<<"\n";
  cin>>n;
 }
 void compute();
};

void har:: compute()
{
 int rem,a,s=n;
 sum=0;
 while(n>0)
 {
  rem=n%10;
  sum=sum+rem;
  n=n/10;
 }
 a=s%sum;
 if(a==0)
 {
  cout<<"Entered number is harshal number\n";
 }
 else
 {
  cout<<"Entererd number is not a harshal number\n";
 }
}

int main()
{
 har h;
 h.getdata();
 h.compute();
 return 0;
}

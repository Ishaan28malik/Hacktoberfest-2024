#include<iostream>

using namespace std;

class pal
{
 private:
 int n,x;
 public:
 void getdata(int);
 void compute();
};

void pal::getdata(int x)
{
 n=x;
}



void pal::compute()
{
 int rem=0,p,rev=0;
 p=n;
 while(n>0)
 {
  rem=n%10;
  rev=rev*10+rem;
  n=n/10;
 }
 if(rev==p)
 {
  cout<<"Entered number is palindrome\n";
 }
 else
 {
  cout<<"Entered number is not a palindrome\n";
 }
}

int main()
{
 int x;
 pal s;
 cout<<"Enter the number"<<"\n";
 cin>>x;
 s.getdata(x);
 s.compute();
 return 0;
}

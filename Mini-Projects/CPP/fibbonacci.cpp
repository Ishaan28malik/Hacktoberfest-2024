#include<iostream>

using namespace std;

class fib
{
 private:
 int n,f1,f2;
 public:
 void inputdata();
 void outputdata();
};

void fib::inputdata()
{
 cout<<"enter the number\n";
 cin>>n;
}

void fib::outputdata()
{
 int i,j;
 int f3=0;
 f1=0;
 f2=1;
 for(i=2;i<n;i++)
 {
  f3=f1+f2;
  f1=f2;
  f2=f3;
  if(f3==n)
  {
  j=1;
  }
 }
 if(j==1)
 {
 cout<<"it is a fibonacci no.\n";
 }
 else
 {
 cout<<"it is not a fibonacci no.\n";
 }
}

int main()
{
 fib c;
 c.inputdata();
 c.outputdata();
 return 0;
}


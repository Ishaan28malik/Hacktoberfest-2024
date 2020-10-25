#include<iostream>
#include <stdio.h>

using namespace std;
int main() {
   //principle amount
   float p = 5;
   //time
   float r = 4;
   //rate in years
   float t = 5;
   // Simple interest
   float SI = 0;
   SI =(p * t * r) / 100;
   printf("Simple Interest = %f ",SI);
  
   return 0;
}

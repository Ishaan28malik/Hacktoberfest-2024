//if-else
void main()
{
  int a , b;
  a = 5;
  b = 4;
  
  //1st type
  if(a > b)
  {
    print('a is greater');
  }
  
  //2nd type
  if(a > b)
  {
    print('a is greater');
  }else{
    print('b is greater');
  }
  
  //3rd type
  (a > b)?print('a is greater'):print('b is greater'); //ternary operator
}

//if you want to run codes at below first remove or comment upper part then then uncomment the below part and hit run.

// //love calculator
// import 'dart:math';
// void main(){
//   loveCalculator();
  
// }

// void loveCalculator(){
//   int loveScore = Random().nextInt(100)+1;
//   print('your love score is $loveScore');
  
//   if(loveScore>70)
//   {
//     print('today is your day ,you both love each other');
//   }else if(loveScore>50)
//   {
//     print('you both are falling in love');
//   }else{
//     print('you both like each other');
//   }
// }
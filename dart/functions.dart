//creating a function like this
//void nameOfFuntion(){ //do something }   -- this type of function is called named function
// (){//do something }   ----this is called anonymous funtion


void main()
{
  //1st type
  int value = sum();
  print('sum is $value');
  
  //2nd type
  var value2 = sum2(5,6);
  print('sum2 is $value2');
  
  //3rd type
  welcomeAndGoodbyeNote(name:'Sayan',note:'welcome'); 
  welcomeAndGoodbyeNote(note:'goodbye',name:'Sayan');
  
  
}

int sum() // why Type is int , cause value returns integer 
{
  int a,b;
  a=5;
  b=6;
  return a+b;
}

int sum2(int a,int b)
{
  return a+b;
}

void welcomeAndGoodbyeNote({String name,String note} )
{
  print('$note $name');
}

//we can use arrow (=>) function 
//like this void main() => runApp(myApp());  --it is used when we have only one statement to execute.
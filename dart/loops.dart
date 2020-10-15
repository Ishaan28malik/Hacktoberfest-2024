void main(){
//   runningSong(99);
  pieMaker();
  
}

void runningSong(int num){
  for(int i = num;i>=1;i--)
  {
    print('$i bottles of beer on the wall, $i bottles of beer');
    print('Take one down and pass it around, ${i-1} bottles of beer on the wall.');
    print("");
  }
}
List<String> fruits =[
  'apple',
  'banana',
  'pear',
  'orange'
];

void pieMaker(){
  for(String fruit in fruits){
    print(fruit+' pie');
  }
  
}
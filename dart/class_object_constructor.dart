//class object and constructor 
//beginner level constructor
void main(){
  //creating a object called 'jenny'
  Human jenny = Human(15);
  //now accessing method talk
  jenny.talk('hello world');
  print('i am ${jenny.height} years old');
}

class Human{
  //properties
  double height;
  int age=1;
  
  //constructor
  Human(double startingHeight){
    height = startingHeight;
  }
  
  //methods
  void talk(String speak){
    print(speak);
  }
  
}
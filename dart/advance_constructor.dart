//class object and constructor 
//beginner level constructor
void main(){
  //creating a object called 'jenny'
  Human jenny = Human(15);
  //now accessing method talk
  jenny.talk('hello world');
  print('i am ${jenny.height} years old');
  
  //operation on advance constructor
  Human2 sam = Human2(height:10,weight:20);
  print('his height is ${sam.height} and ${sam.weight}');
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

// advance level of constructor
class Human2{
  double height;
  double weight;
  
  //creating a constructor 
  Human2({this.height,this.weight});
}
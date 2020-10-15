
void main(){
  Car lambo = Car();
  lambo.drive();
  
  ElectricCar tesla = ElectricCar();
  tesla.drive();
  print(tesla.numberOfSeats);
  
}

class Car{
  int numberOfSeats = 5;
  
  void drive(){
    print('running car');
  }
}
// inheritance
class ElectricCar extends Car{
  int battery = 100;
  
  void batteryLife(){
    battery = 100;
  }
}
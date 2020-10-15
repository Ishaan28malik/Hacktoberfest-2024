void main(){
//   Car lambo = Car();
//   lambo.drive();
  
//   ElectricCar tesla = ElectricCar();
//   tesla.drive();
//   print(tesla.numberOfSeats);
  SelfDrivingCar nvidia = SelfDrivingCar();
  print(nvidia.battery);
  nvidia.drive();
  
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
//polymorphism
class SelfDrivingCar extends Car{
  int battery = 100;
  @override
  void drive(){
    print('running more fater');
  }
}
void main(){
  Car myCar = Car(carStyle : CarType.lambo);
}

class Car{
  CarType carStyle;
  
  Car({this.carStyle});
  
}

enum CarType{
  suv,
  cupe,
  lambo,
  hatchback
}
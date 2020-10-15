class Main {
 public static void main (String[] args) {
   Person hasargs = new Person("Jane", 42, "female", true, true, true, true);
    Person noargs = new Person();
    //Draw Args Person
    hasargs.drawHair();
    hasargs.drawTopFace();
    hasargs.drawBotFace();
    hasargs.drawBody();
    hasargs.drawLower();
    System.out.println(hasargs);
    //Set new values for Args
    hasargs.setAge(100);
    hasargs.setHair(false);
    hasargs.setSmile(false);
    hasargs.setTee(false);
    hasargs.setWink(false);
    //Use drawPerson()
    hasargs.drawPerson();
    System.out.println(hasargs);
    //Draw No Args Person
    noargs.drawHair();
    noargs.drawTopFace();
    noargs.drawBotFace();
    noargs.drawBody();
    noargs.drawLower();
    System.out.println(noargs);
    //Set new values for No Args
    noargs.setAge(160);
    noargs.setHair(true);
    noargs.setSmile(true);
    noargs.setTee(true);
    noargs.setWink(true);
    //Use drawPerson()
    noargs.drawPerson();
    System.out.println(noargs);
 }
}

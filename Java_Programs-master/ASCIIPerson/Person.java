 class Person {
   private String name;
   private int age;
   private String gender;
   private boolean hair;
   private boolean tee;
   private boolean wink;
   private boolean smile;

  public Person (String name1, int age1, String gender1, boolean hair1, boolean tee1, boolean wink1, boolean smile1) {
    name = name1;
    age = age1;
    gender = gender1;
    hair = hair1;
    tee = tee1;
    wink = wink1;
    smile = smile1;
  }
  public Person () {
    name = "John Doe";
    age = 21;
    gender = "male";
    hair = false;
    tee = false;
    wink = false;
    smile = false;
  }
  public String getName(){
    return name;
  }
  public int getAge(){
    return age;
  }
  public boolean getHair(){
    return hair;
  }
  public boolean getTee(){
    return tee;
  }
  public boolean getWink(){
    return wink;
  }
  public boolean getSmile(){
    return smile;
  }
  public String getGender() {
    return gender;
  }
  public void setAge(int newAge){
    age = newAge;
  }
  public void setHair(boolean newHair) {
    hair = newHair;
  }
  public void setTee(boolean newTee) {
    tee = newTee;
  }
  public void setWink(boolean newWink) {
    wink = newWink;
  }
  public void setSmile(boolean newSmile) {
    smile = newSmile;
  }
  public void drawHair() {
   if (hair) {
      System.out.println("           ||||||||||||||||||||||           "); 
      System.out.println("           ||||||||||||||||||||||           "); 
   } else {
      System.out.println("                                            ");
   }
  }
  public void drawTopFace() {
    if (wink) {
      System.out.println("           [--------------------]           ");
      System.out.println("           |                    |           ");
      System.out.println("           |   ___              |           ");
      System.out.println("           |  (___)       ____  |           ");
      System.out.println("           |                    |           ");
    } else {
      System.out.println("           [--------------------]           ");
      System.out.println("           |                    |           ");
      System.out.println("           |   ___        ___   |           ");
      System.out.println("           |  (___)      (___)  |           ");
      System.out.println("           |                    |           ");
    }
  }
  public void drawBotFace() {
    if (smile) {
      System.out.println("           |         <          |           ");
      System.out.println("           |  ________________  |           ");
      System.out.println("           |  |______________|  |           ");
      System.out.println("           |  \\______________/  |           ");
      System.out.println("           [--------------------]           ");
    } else {
      System.out.println("           |         <          |           ");
      System.out.println("           |   ______________   |           ");
      System.out.println("           |  / ____________ \\  |           ");
      System.out.println("           | /_/            \\_\\ |           ");
      System.out.println("           [--------------------]           ");
    }
  }
  public void drawBody() {
    if (tee) {
      System.out.println("[------------------------------------------]");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|__________|   AP COMP SCIENCE  |__________|");
      System.out.println("|          |       IS EPIC      |          |");
      System.out.println("|          |         :O         |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("[------------------------------------------]");
    } else {
      System.out.println("[------------------------------------------]");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |   AP COMP SCIENCE  |          |");
      System.out.println("|          |       IS EPIC      |          |");
      System.out.println("|          |         :O         |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|          |                    |          |");
      System.out.println("|__________|                    |__________|");
      System.out.println("|          |                    |          |");
      System.out.println("[------------------------------------------]");
    }
  }
    public void drawLower() {
      System.out.println("           [--------------------]           ");
      System.out.println("           |  /      |       \\  |           ");
      System.out.println("           | /       |        \\ |           ");
      System.out.println("           |/        |         \\|           ");
      System.out.println("           |         |          |           ");
      System.out.println("           |         |          |           ");
      System.out.println("           |         |          |           ");
      System.out.println("           |         |          |           ");
      System.out.println("           |         |          |           ");
      System.out.println("           |         |          |           ");
      System.out.println("           |         |          |           ");
      System.out.println("           |         |          |           ");
      System.out.println("           [--------------------]           ");  
  }
  public void drawPerson(){
    drawHair();
    drawTopFace();
    drawBotFace();
    drawBody();
    drawLower();
  }
  public String toString() {
      String person = name + " is a " + age + " year old " + gender + ". It is " + hair + " that they have hair and it is " + tee;
      person = person + " that they like wearing a tee. Additionally, it is " + wink + " that they can wink and ";
      person += smile + " that they like to smile.";
      return person;
  }
}      

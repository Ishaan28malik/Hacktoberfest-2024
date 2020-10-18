void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
int a,b;
}

void loop() {
  int a,b,j;
  // put your main code here, to run repeatedly:
Serial.println("ao dekho");
while(!Serial.available()){
  
}
a=Serial.read();
while(!Serial.available()){
}
Serial.println(a);

b=Serial.read();
while(!Serial.available()){
}
Serial.println(b);

j=a+b;
Serial.println(j);
}

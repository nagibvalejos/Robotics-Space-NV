void setup(){
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
}

void loop(){
  digitalWrite(3,1);  // color blanco
  digitalWrite(4,1);
  digitalWrite(5,1);
  delay(500);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,0);
  delay(500);
  digitalWrite(3,1);
  digitalWrite(4,1);
  digitalWrite(5,1);
  delay(500);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,0);
  delay(500);
  digitalWrite(3,1);
  digitalWrite(4,1);
  digitalWrite(5,1);
  delay(500);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,0);
  delay(500);
  //encendido escalar
  digitalWrite(6,1);  //rojo
  delay(500);
  digitalWrite(7,1);  //amarillo
  delay(500);
  digitalWrite(8,1);  //verde
  delay(500);
  digitalWrite(8,0);  //VERDE
  delay(500);
  digitalWrite(7,0);  //AMARILLO
  delay(500);
  digitalWrite(6,0);  //ROJO
  delay(500);
}

void setup(){
  pinMode(3,OUTPUT); //r
  pinMode(4,OUTPUT); //a
  pinMode(5,OUTPUT); //v
  pinMode(6,OUTPUT); //rojo
  pinMode(7,OUTPUT); //amarillo
  pinMode(8,OUTPUT); //verde
}

void loop(){
  digitalWrite(6,1); 
  delay(500);  
  digitalWrite(6,0);
  digitalWrite(7,1);
  delay(500);  
  digitalWrite(7,0);
  digitalWrite(8,1);
  delay(500);  
  digitalWrite(8,0); 
  //RGB cian
  digitalWrite(3,0);
  digitalWrite(4,1); 
  digitalWrite(5,1);
  delay(500);  
  //RGB azul
  digitalWrite(3,0);
  digitalWrite(4,1); 
  digitalWrite(5,0);
  delay(500);  
  //RGB magenta
  digitalWrite(3,1);
  digitalWrite(4,1); 
  digitalWrite(5,0);
  delay(500);
  //RGB blanco
  digitalWrite(3,1);
  digitalWrite(4,1); 
  digitalWrite(5,1);
  delay(500); 
  //apagado
  digitalWrite(3,0);
  digitalWrite(4,0); 
  digitalWrite(5,0);
  delay(1000);
}

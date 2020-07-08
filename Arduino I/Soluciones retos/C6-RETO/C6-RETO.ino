int r=6, a=7, v=8;
int R=9, G=11, B=10;      
void setup(){
  for(int u=6;u<=11;u++){
    pinMode(u,OUTPUT);
  }
}

void loop() {
  for(int j=6;j<=8;j++){
    digitalWrite(j,1);
    delay(250);
    digitalWrite(j,0);
  } 
  analogWrite(G,255);
  analogWrite(B,255); //CIAN
  delay(250); 
  analogWrite(G,0);   //AZUL
  delay(250);
  analogWrite(R,255); //MAGENTA
  delay(250);
  analogWrite(G,255); //BLANCO
  delay(250);
  for(int j=9;j<=11;j++){ //APAGADO
    analogWrite(j,0);
  } 
  delay(1000);
}

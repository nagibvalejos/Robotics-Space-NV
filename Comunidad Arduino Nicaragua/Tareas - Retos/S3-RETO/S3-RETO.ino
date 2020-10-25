int ledV=8, ledA=7, ledR=6;   //constantes
int pulsador=5, pulsador2=4;  //constantes 
int p1=0, p2=0; //variables
void setup(){
  pinMode(ledV,OUTPUT);
  pinMode(ledA,OUTPUT);
  pinMode(ledR,OUTPUT);
  pinMode(pulsador,INPUT);
  pinMode(pulsador2,INPUT_PULLUP);  //logica inversa
}

void loop() {
  p1=digitalRead(pulsador);
  p2=digitalRead(pulsador2);
  if(p1){//if(p1==1) if(p1==HIGH)
    digitalWrite(ledR,1);
    digitalWrite(ledA,1);
    digitalWrite(ledV,1);
  }
  else{
    digitalWrite(ledR,0);
    digitalWrite(ledA,0);
    digitalWrite(ledV,0);
  }
  if(p2==0){
    digitalWrite(ledR,1);
    delay(500);
    digitalWrite(ledA,1);
    delay(500);
    digitalWrite(ledV,1);
    delay(500);
    digitalWrite(ledV,0);
    delay(500);
    digitalWrite(ledA,0);
    delay(500);
    digitalWrite(ledR,0);
    delay(500);
  }
}

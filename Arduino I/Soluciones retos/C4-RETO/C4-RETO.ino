int ledV=8;      
int ledA=7;      
int ledR=6;
int pulsador=5;   
int pulsador2=4; 
int p1=0;       
int p2=0;
void setup(){
  pinMode(pulsador,INPUT);
  pinMode(pulsador2,INPUT_PULLUP);
  pinMode(ledR,OUTPUT);
  pinMode(ledA,OUTPUT);
  pinMode(ledV,OUTPUT);
}
void loop(){
  p1=digitalRead(pulsador);
  if(p1){
    digitalWrite(ledA,1);
    digitalWrite(ledR,1);
    digitalWrite(ledV,1);
  }
  else{
    digitalWrite(ledA,0);
    digitalWrite(ledR,0);
    digitalWrite(ledV,0);
  }
  p2=digitalRead(pulsador2);
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

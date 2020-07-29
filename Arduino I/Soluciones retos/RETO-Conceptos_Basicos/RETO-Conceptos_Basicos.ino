int r=8, a=7, v=6, R=11, G=9, B=10;
int p1=12, p2=13, pi, pd;
int potR=A2, potG=A1, potB=A0,
lecturaR, lecturaG, lecturaB,
Red, Green, Blue;
void setup(){
  for(int i=6;i<=11;i++){
    pinMode(i,OUTPUT);
  }
  pinMode(p1,INPUT_PULLUP);
  pinMode(p2,INPUT);
  Serial.begin(9600);
}

void loop(){
  pi=digitalRead(p1);
  pd=digitalRead(p2);
  if(pi==0){
    int aleatorio=random(0,10);
    Serial.print("El numero aleatorio izquierdo es:");
    Serial.println(aleatorio);
    for(int i=0;i<aleatorio;i++){
      digitalWrite(r,1);
      digitalWrite(a,1);
      digitalWrite(v,1); 
      delay(250);
      digitalWrite(r,0);
      digitalWrite(a,0);
      digitalWrite(v,0); 
      delay(250); 
    }
  }
  if(pd){
    int aleatorio=random(0,5);
    Serial.print("El numero aleatorio derecho es:");
    Serial.println(aleatorio);
    for(int i=0;i<aleatorio;i++){
      for(int j=6;j<=8;j++){
        digitalWrite(j,1);
        delay(250);
      }
      for(int j=8;j>=6;j--){
        digitalWrite(j,0);
        delay(250);
      }
    }
  }
  if(pi==1 and pd==0){
    digitalWrite(r,1);
    delay(250);
    digitalWrite(r,0);
    delay(250);
    digitalWrite(a,1);
    delay(250);
    digitalWrite(a,0);
    delay(250);
    digitalWrite(v,1);
    delay(250);
    digitalWrite(v,0);
    delay(250);
  }
  lecturaR=analogRead(potR);
  Red=map(lecturaR,0,1023,0,255);
  analogWrite(R,Red);
  lecturaG=analogRead(potG);    
  Green=map(lecturaG,0,1023,0,255);
  analogWrite(G,Green);
  lecturaB=analogRead(potB);    
  Blue=map(lecturaB,0,1023,0,255);
  analogWrite(B,Blue);
  Serial.print(Red);
  Serial.print(",");
  Serial.print(Green);
  Serial.print(",");
  Serial.println(Blue);
}

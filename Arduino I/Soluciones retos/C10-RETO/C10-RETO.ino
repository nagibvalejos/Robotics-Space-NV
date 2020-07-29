int echo=6,trig=7,
ledR=8, ledA=9, ledV=10;
long duracion, distancia;
void setup() {
  pinMode(ledR,OUTPUT);
  pinMode(ledA,OUTPUT);
  pinMode(ledV,OUTPUT);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  Serial.begin(9600);
}
void loop() {
  digitalWrite(trig,0);
  delayMicroseconds(2);
  digitalWrite(trig,1);
  delayMicroseconds(10);
  digitalWrite(trig,0);
  duracion=pulseIn(echo,1);
  distancia=(duracion /2)/29;
  if(distancia<15){
    Serial.println("Semaforo encendido");
    digitalWrite(ledR,1);
    delay(1000);
    digitalWrite(ledR,0);
    delay(1000);
    digitalWrite(ledA,1);
    delay(700);
    digitalWrite(ledA,0);
    delay(700);
    digitalWrite(ledV,1);
    delay(1000);
    digitalWrite(ledV,0);
    delay(1000);
    digitalWrite(ledA,1);
    delay(300);
    digitalWrite(ledA,0);
    delay(300);
  }
}

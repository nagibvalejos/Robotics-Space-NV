#include <DHT.h>
int ldr=A0, lectura, oscuridad,
ledR=8, ledA=9, ledV=10,
trig=7, echo=6;
long duracion, distancia;
float t,h,i;
DHT sensor(11,DHT11); //DHT22
void setup(){
  pinMode(echo,INPUT);
  for(int i=7;i<=10;i++){
    pinMode(i,OUTPUT);
  }
  Serial.begin(9600);
  sensor.begin();
}

void loop() {
  lectura=analogRead(ldr);
  oscuridad=map(lectura,0,1023,0,100);
  Serial.println("Nivel de oscuridad: "+String(oscuridad)+"%");
  digitalWrite(trig,0);
  delayMicroseconds(2);  
  digitalWrite(trig,1);
  delayMicroseconds(10);
  digitalWrite(trig,0);
  duracion=pulseIn(echo,1);
  distancia=(duracion/2)/29;
  if(oscuridad>60){
    digitalWrite(ledR,1);
    digitalWrite(ledA,1);
    digitalWrite(ledV,1);
    Serial.println("Distancia:"+String(distancia)+"cm");
    if(distancia<10){
      t=sensor.readTemperature();
      h=sensor.readHumidity();
      i=sensor.computeHeatIndex(t,h,true);
      Serial.print("Humedad:"+String(h)+"% HR");    
      Serial.print(" Temperatura:"+String(t)+"ºC");
      Serial.println(" Indice:"+String(i)+"ºC");
    }
  }
  else{
    digitalWrite(ledR,0);
    digitalWrite(ledA,0);
    digitalWrite(ledV,0);
  }
  delay(1000);
}

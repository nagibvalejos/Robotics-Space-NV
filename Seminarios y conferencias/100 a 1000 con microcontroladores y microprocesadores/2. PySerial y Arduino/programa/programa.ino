int lm35 = A0;
void setup() {

  Serial.begin(9600);
  pinMode(lm35,INPUT);
}

void loop() {
  float voltinput = analogRead(lm35);//0-1023
  float  mvolts = ( voltinput/1024.0)*5000;//10mv/°C
  float tempc = mvolts/10;
  Serial.println(tempc);//enviando el valor al puerto serial 5\n

  delay(1000);
}

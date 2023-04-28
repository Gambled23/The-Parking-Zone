const int canSens = 5;
const int triggers[canSens] = {13, 11, 9, 7, 5};
const int echos[canSens] = {12, 10, 8, 6, 4};
long dur, dis;

void setup() {
  Serial.begin(9600);
  for(int i(0); i < canSens; ++i) {
     pinMode(triggers[i], OUTPUT);
     pinMode(echos[i], INPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    if (Serial.read() == 't') {
      for(int i(0); i < canSens; ++i) {
        Serial.print(lectura(triggers[i], echos[i]));
        delay(10);
      }
    }
  }
}

int lectura(int t, int e) {
  digitalWrite(t, LOW);
  delayMicroseconds(2);
  digitalWrite(t, HIGH);
  delayMicroseconds(10);
  digitalWrite(t, LOW);

  dur = pulseIn(e, HIGH);
  dis = dur*0.0343;
  
  if(dis < 20) {
    return(1);
  }
  else {
    return(0);
  }
}

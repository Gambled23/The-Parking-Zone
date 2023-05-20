#include <Servo.h>

Servo motor;

const int canSens = 3, triggers[canSens] = {13, 11, 9}, echos[canSens] = {12, 10, 8};
const int btn1 = A0, btn2 = A1;

long dur, dis;
int anterior1, anterior2, estado1, estado2;
int tipo, estado;

bool avanzar = false;

void setup() {
  Serial.begin(9600);
  for(int i(0); i < canSens; ++i) {
     pinMode(triggers[i], OUTPUT);
     pinMode(echos[i], INPUT);
  }
  pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);
  anterior1 = digitalRead(btn1);
  anterior2 = digitalRead(btn2);

  motor.attach(6);
  motor.write(90);
}

void loop() {
  botones();
  
  if (Serial.available() > 0) {
    if (Serial.read() == 'l') {
      estadoSensores();
    } 
  }
}

void botones() {
  estado1 = digitalRead(btn1);
  estado2 = digitalRead(btn2);

  if (anterior1 == HIGH && estado1 == LOW) {
    tipo = 1;
    Serial.println(tipo);
    if (estadoSensores() == true) {
      estado = 1;
      Serial.println(estado);
      abrir();
    }
    else {
      estado = 2;
      Serial.println(estado);
    }
  }

  if (anterior2 == HIGH && estado2 == LOW) {
    tipo = 2;
    Serial.println(tipo);
    if (estadoSensores() == true) {
      estado = 1;
      Serial.println(estado);
      abrir();
    }
    else {
      estado = 2;
      Serial.println(estado);
    }
  }

  anterior1 = estado1;
  anterior2 = estado2;
}

void abrir() {
  int i = 90;
  while(i >= 0) {
    motor.write(i);
    delay(250);
    i -= 10;
  }
  motor.write(0);
  delay(5000);
  
  i += 10;
  while(i <= 90) {
    motor.write(i);
    delay(250);
    i += 10;
  }
  motor.write(90);
}

bool estadoSensores() {
  bool abrir = false;
  
  for(int i(0); i < canSens; ++i) {
    int sensor = lectura(triggers[i], echos[i]);
    Serial.println(sensor);
    if (sensor == 0) {
      abrir = true;
    }
    delay(500);
  }
  
  return(abrir);
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

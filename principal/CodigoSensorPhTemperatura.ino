#include <Wire.h>
#include <Thermistor.h>

//Variáveis globais
float calibration_value = 21.34 - 0.7; //Valor de calibração para o sensor de pH.
int phval = 0;
unsigned long int avgval;  //Valor médio das leituras analógicas.
int buffer_arr[10], tp; //Array para armazenar leituras analógicas.
float ph_act; //Valor real do pH calculado a partir das leituras analógicas.
int analogPinTp = A0;
Thermistor temp(2);
int ledPinos[] = {3,4,5,6};
int numLEDs = 4;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  for(int a = 0; a < numLEDs; a++) {
    pinMode(ledPinos[a], OUTPUT);
    digitalWrite(ledPinos[a], LOW);
  }
}

void loop() {
  //(leitura analógica e ordenação do buffer)
  for (int i = 0; i < 10; i++) {
    buffer_arr[i] = analogRead(A0);
    delay(30);
  }
  
  for (int i = 0; i < 9; i++) {
    for (int j = i + 1; j < 10; j++) {
      if (buffer_arr[i] > buffer_arr[j]) {
        tp = buffer_arr[i];
        buffer_arr[i] = buffer_arr[j];
        buffer_arr[j] = tp;
      }
    }
  }

  avgval = 0;
  for (int i = 2; i < 8; i++)
    avgval += buffer_arr[i];

  float volt = (float)avgval * 5.0 / 1024 / 6;
  ph_act = -5.70 * volt + calibration_value;

  Serial.print("pH Val: ");
  Serial.print(ph_act);
  //(leitura da temperatura)
  int temperature = temp.getTemp();
  if(temperature < 0) {
    int temperatura = (-1)*temperature;
    Serial.print(" | Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" °C");
  } else {
    Serial.print(" | Temperatura: ");
    Serial.print(temperature);
    Serial.println(" °C");
  }
  delay(1000);
  // Controle dos LEDs com base no comando recebido pela porta serial.
  if(Serial.available()>0){
    char comando = Serial.read();
    if(comando == 'A') {
      digitalWrite(ledPinos[0], HIGH);
    } else if(comando == 'B') {
      digitalWrite(ledPinos[1], HIGH);
    } else if(comando == 'C') {
      digitalWrite(ledPinos[2], HIGH); 
    } else if(comando == 'D') {
      digitalWrite(ledPinos[3], HIGH);
    }
  }
}

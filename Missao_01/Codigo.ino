const byte LED = 13;

void setup(){
  pinMode(LED, OUTPUT);
}

void loop(){
  blink(LED, 2000, 6000);
  blink(LED, 1000, 6000);
  blink(LED, 500, 6000);
  return;
}

/* 
Função responsável por fazer um determinado LED piscar em 
um período x de tempo durante um tempo total y em ms.
*/
void blink(byte LED, int PERIODO, int TEMPO){
  int FREQUENCIA = TEMPO / PERIODO;
  
  for(int i = 0; i < FREQUENCIA; i++){
    digitalWrite(LED, HIGH);
	delay(PERIODO / 2);
    digitalWrite(LED, LOW);
  	delay(PERIODO / 2);
  }
}
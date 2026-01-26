//Motion Detection & Toilet Light Turn ON
 int signal = 0;
void setup(){
  pinMode(0, INPUT);//pir sensor input
  pinMode(1, OUTPUT);//relay 
}

void loop()
{
  signal = digitalRead(0);
  
  if (signal == 1){
    digitalWrite(1, HIGH);	
    delay(10000);
  }	//increase the delay as per your time required...
   
  else{digitalWrite(1, LOW);}
}

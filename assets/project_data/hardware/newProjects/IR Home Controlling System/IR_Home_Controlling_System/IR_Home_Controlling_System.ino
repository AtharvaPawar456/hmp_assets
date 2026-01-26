#include <IRremote.h>
int IRpin = 4;

int RED = 9;
int GREEN = 8;
int BLUE = 7;
int WHITE = 6;

IRrecv irrecv(IRpin);
decode_results results;

void setup() {
Serial.begin(9600);
irrecv.enableIRIn();

pinMode(RED, OUTPUT);
pinMode(GREEN, OUTPUT);
pinMode(BLUE, OUTPUT);
pinMode(WHITE, OUTPUT);

digitalWrite(RED, LOW);
digitalWrite(GREEN, LOW);
digitalWrite(BLUE, LOW);
digitalWrite(WHITE, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
    if(irrecv.decode(&results)){
      int IRvalue = results.value;
      Serial.println(IRvalue);
      delay(10);
               //ON :   16236607                3457774333
        if (IRvalue == -16321 || IRvalue == 29437 ){         
              digitalWrite(RED,   HIGH);
              digitalWrite(GREEN, HIGH);
              digitalWrite(BLUE,  HIGH);
              digitalWrite(WHITE, HIGH);}//ON
    
                //OFF : 16203967                 3571254145
        if (IRvalue == 897 || IRvalue == 16575 ){         
              digitalWrite(RED,   LOW);
              digitalWrite(GREEN, LOW);
              digitalWrite(BLUE,  LOW);
              digitalWrite(WHITE, LOW);}//OFF

//ON
//'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        if (IRvalue == 8415 || IRvalue == 21217 ){            digitalWrite(RED, HIGH);}
              //Ch1-R : 8415                 21217
    
        if (IRvalue == -23331 || IRvalue == -24481 ){         digitalWrite(GREEN, HIGH);}
              //Ch2-G : -23331                 -24481
    
        if (IRvalue == 9029 || IRvalue == 24735 ){            digitalWrite(BLUE, HIGH);}
              //Ch3-B : 9029                 24735
    
        if (IRvalue == -8161 || IRvalue == -27967 ){          digitalWrite(WHITE, HIGH);}
              //Ch4-W : -8161                 -27967

//OFF
//'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

        if (IRvalue == 4335 || IRvalue == -25983 ){            digitalWrite(RED, LOW);}
              //Ch1-O : 4335              -25983
    
        if (IRvalue == -4995 || IRvalue == -28561 ){         digitalWrite(GREEN, LOW);}
              //Ch2-LG : -4995             -28561
    
        if (IRvalue == 157 || IRvalue == 20655 ){            digitalWrite(BLUE, LOW);}
              //Ch3-LB : 157        20655
    
        if (IRvalue == -12241 || IRvalue == 23521 ){          digitalWrite(WHITE, LOW);}
              //Ch4-Flash : -12241          23521

//'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''           
      irrecv.resume();

  }
}

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <IRremote.h>

#include "DHT.h"
#define DHTPIN 3     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x3F, 16,2);


//IR Receiver Data Pin
int IRpin = 4;
IRrecv irrecv(IRpin);
decode_results results;

//Chaneel Pin Declaration
int RED = 12;
int GREEN = 11;
int BLUE = 10;
int WHITE = 9;

//Variable Declaration
int Rval = 0;
int Gval = 0;
int Bval = 0;
int Wval = 0;

float h = 0.0;
float t = 0.0;
int count = 0;

int TEMP = t;
int HUM = h;

//'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

void setup(){
  lcd.init();   
  lcd.backlight();
  lcd.clear(); 

  Serial.begin(9600);
  irrecv.enableIRIn();
  dht.begin();

  pinMode(RED,    OUTPUT);
  pinMode(GREEN,  OUTPUT);
  pinMode(BLUE,   OUTPUT);
  pinMode(WHITE,  OUTPUT);

  //Set All Channel as OFF at Start
  digitalWrite(RED,   LOW);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE,  LOW);
  digitalWrite(WHITE, LOW);

  void DHTval();
  void displaydata();
}

void loop(){
if (count == 100){   DHTval();   displaydata();}

//'''''''''''''''''''''''''''''''''''''''''''''
//Main Code
//
    if(irrecv.decode(&results)){
      int IRvalue = results.value;
      Serial.println(IRvalue);
      delay(10);
               //ON :   16236607                3457774333
        if (IRvalue == -16321 || IRvalue == 29437 ){         
              digitalWrite(RED,   HIGH);
              digitalWrite(GREEN, HIGH);
              digitalWrite(BLUE,  HIGH);
              digitalWrite(WHITE, HIGH);
                Rval = 1;
                Gval = 1;
                Bval = 1;
                Wval = 1;}//ON
    
                //OFF : 16203967                 3571254145
        if (IRvalue == 897 || IRvalue == 16575 ){         
              digitalWrite(RED,   LOW);
              digitalWrite(GREEN, LOW);
              digitalWrite(BLUE,  LOW);
              digitalWrite(WHITE, LOW);
                Rval = 0;
                Gval = 0;
                Bval = 0;
                Wval = 0;}//OFF

        //ON
        //'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        if (IRvalue == 8415 || IRvalue == 21217 ){            digitalWrite(RED, HIGH);    Rval = 1;}
              //Ch1-R : 8415                 21217
    
        if (IRvalue == -23331 || IRvalue == -24481 ){         digitalWrite(GREEN, HIGH);  Gval = 1;}
              //Ch2-G : -23331                 -24481
    
        if (IRvalue == 9029 || IRvalue == 24735 ){            digitalWrite(BLUE, HIGH);   Bval = 1;}
              //Ch3-B : 9029                 24735
    
        if (IRvalue == -8161 || IRvalue == -27967 ){          digitalWrite(WHITE, HIGH);  Wval = 1;}
              //Ch4-W : -8161                 -27967

        //OFF
        //'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        if (IRvalue == 4335 || IRvalue == -25983 ){            digitalWrite(RED, LOW);  Rval = 0;}
              //Ch1-O : 4335              -25983
    
        if (IRvalue == -4995 || IRvalue == -28561 ){         digitalWrite(GREEN, LOW);  Gval = 0;}
              //Ch2-LG : -4995             -28561
    
        if (IRvalue == 157 || IRvalue == 20655 ){            digitalWrite(BLUE, LOW);   Bval = 0;}
              //Ch3-LB : 157        20655
    
        if (IRvalue == -12241 || IRvalue == 23521 ){          digitalWrite(WHITE, LOW); Wval = 0;}
              //Ch4-Flash : -12241          23521

      irrecv.resume();
      }

//'''''''''''''''''''''''''''''''''''''''''''''
// Display Channel + Temp + Hum



  lcd.setCursor(0,0);
  lcd.print("R G B W Temp Hum");
  
  lcd.setCursor(0,1);
  lcd.print(Rval);
  lcd.setCursor(2,1);
  lcd.print(Gval);
  lcd.setCursor(4,1);
  lcd.print(Bval);
  lcd.setCursor(6,1);
  lcd.print(Wval);
  lcd.setCursor(9,1);
  lcd.print(TEMP);
  lcd.setCursor(14,1);
  lcd.print(HUM);

  count = count + 1;
  delay(100);
}
 

void DHTval(){
  h = dht.readHumidity();
            // Read temperature as Celsius (the default)
  t = dht.readTemperature();
  
            // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
  }
  TEMP = t;
  HUM = h;
  count = 0;  

}


void displaydata(){                   // Serial Monitor Code:
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.println(F("% "));
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(F("°C "));
  //'''''''''''''''''''''''''''''''''''''''''''''
  Serial.println("Channel: ");
  Serial.println("RED: ");
  Serial.println(Rval);
  Serial.println("GREEN: ");
  Serial.println(Gval);
  Serial.println("BLUE: ");
  Serial.println(Bval);
  Serial.println("White: ");
  Serial.println(Wval);
  Serial.println(" ");
}

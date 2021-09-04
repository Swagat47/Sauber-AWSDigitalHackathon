/*
 * ------------------------------------------------------- *
 Team Sauber
 AWS Digital Hackathon
 Theme: Agriculture - Post Harvest Management
 Project Title: Smart Sanitization Storage Room (SSS-Room)
 * ------------------------------------------------------- *
*/

// Global Variables
int LED = 2;
int PIR = 4;

void setup() {
  //Initialising Variables 
  pinMode(LED,OUTPUT);
  pinMode(PIR,INPUT);
  Serial.begin(9600);

}

void loop() {
  //Main code
  if(digitalRead(PIR)==HIGH){ 
    digitalWrite(LED,HIGH);
    Serial.println("Insects/pests Detected - Destroying their DNA");
    delay(3000); // wait for 100 milliseconds
  }
  else
  {
    digitalWrite(LED,LOW);
    Serial.println("Status : ALL Good")  ;
    delay(100); //wait for 1000 milliseconds
  }
}

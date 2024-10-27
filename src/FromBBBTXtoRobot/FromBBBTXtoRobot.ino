#include <Braccio.h>
#include <Servo.h>

Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;

int indexSpeed;
int indexBase;
int indexShoulder;
int indexElbow;
int indexWristRot;
int indexWristVer;
int indexGripper;
String Speed;
String Base;
String Shoulder;
String Elbow;
String WristRot;
String WristVer;
String Gripper;
char fromBBB;
String temp="";

int incomingByte = 0; // for incoming serial data

int red_light_pin= 2; 
int green_light_pin = 4; 
int blue_light_pin = 8;

void setup() {
  RGB_color(255, 0, 0); // green
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
    // set up the LCD's number of columns and rows:
  Braccio.begin();
  //pinMode(2,OUTPUT);
  //pinMode(4,OUTPUT);
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
}
// recvString = "10,90,90b"
void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(red_light_pin, red_light_value);
  analogWrite(green_light_pin, green_light_value);
  analogWrite(blue_light_pin, blue_light_value);
}
void loop() {
  //digitalWrite(2,LOW);
  //digitalWrite(4,HIGH);
  RGB_color(0, 0, 255); // green
    if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    RGB_color(0, 0, 0); // green
    RGB_color(255, 0, 0); // green
    // read the incoming byte
 //   delay(100);
    fromBBB = char(incomingByte);
//    if (fromBBB == 'a'){
//      indexmov = temp.indexOf(',');
//      nbrMov = temp.substring(0, indexmov);
//      
//    }
//    
    if (fromBBB == 'b'){
      indexSpeed = temp.indexOf(',');
      Speed = temp.substring(0, indexSpeed);
      
      indexBase = temp.indexOf(',', indexSpeed+1);
      Base = temp.substring(indexSpeed+1, indexBase);
      
      indexShoulder = temp.indexOf(',', indexBase+1);
      Shoulder = temp.substring(indexBase+1, indexShoulder);
      
      indexElbow = temp.indexOf(',', indexShoulder+1);
      Elbow =temp.substring(indexShoulder+1, indexElbow);
      
      indexWristRot = temp.indexOf(',', indexElbow+1);
      WristRot = temp.substring(indexElbow+1, indexWristRot);
      
      indexWristVer = temp.indexOf(',', indexWristRot+1);
      WristVer = temp.substring(indexWristRot+1, indexWristVer);
//      indexWristVer = temp.indexOf(',', indexElbow+1);
//      WristVer = temp.substring(indexElbow+1, indexWristVer);
//
//      indexWristRot = temp.indexOf(',', indexWristVer+1);
//      WristRot = temp.substring(indexWristVer+1, indexWristRot);
        
      indexGripper = temp.indexOf('b', indexWristVer+1);
      Gripper = temp.substring(indexWristVer+1, indexGripper);

      Braccio.ServoMovement(Speed.toInt(), Base.toInt(), Shoulder.toInt(), Elbow.toInt(), WristRot.toInt(), WristVer.toInt(), Gripper.toInt()); 
      temp = ""; 
    }
    else {
      temp = temp + fromBBB;
    }
  }
}

/*Example sketch to control a stepper motor with A4988 stepper motor driver and Arduino without a library. More info: https://www.makerguides.com */

#include <ezButton.h>

ezButton button(0);
#define stepsPerRevolution 200

// Define stepper motor direction and step pins
//#define direction_L 2
//#define step_L 3
#define direction_R 4
#define step_R 5

// Define sensor max and min for each side
#define sensor_R_min A0
#define sensor_R_max A1
//#define sensor_L_min A2
//#define sensor_L_max A3

// Initialize each sensor state as zero
int sensor_R_min_state = 0;  //
int sensor_R_max_state = 0;
//int sensor_L_min_state = 0;         // variable for reading the pushbutton status
//int sensor_L_max_state = 0;

// Digits
#define ones_A 6
#define ones_B 7
#define ones_C 8
#define ones_D 9
#define tens_A 10
#define tens_B 11
#define tens_C 12
#define tens_D 13

// MSB >> DCBA << LSB
const int ones[4] = {6, 7, 8, 9};
const int tens[4] = {10, 11, 12, 13};
// see 74LS48 datasheet for correct output
// 0 through 9
//const byte numbers[10] = {0b0000, 0b1000, 0b0100, 0b1100, 0b0010, 0b1010, 0b0110, 0b1110, 0b0001, 0b1001};
const byte numbers[10] = {0b0000, 0b0001, 0b0010, 0b0011, 0b0100, 0b0101, 0b0110, 0b0111, 0b1000, 0b1001};

unsigned long start_R;
unsigned long stop_R;
unsigned long time_R;

void setup() {
  // Declare pins as output:
  button.setDebounceTime(50);
  pinMode(direction_R, OUTPUT);
  pinMode(step_R, OUTPUT);
  //pinMode(direction_L, OUTPUT);
  //pinMode(step_L, OUTPUT);
  
  pinMode(sensor_R_min, INPUT);
  pinMode(sensor_R_max, INPUT);
  //pinMode(sensor_L_min, INPUT);
  //pinMode(sensor_L_max, INPUT);

  // Digits
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);


  Serial.begin(9600);
  
  // Home to minimum position
  digitalWrite(direction_R, LOW);
  sensor_R_min_state = analogRead(sensor_R_min);
  sensor_R_max_state = analogRead(sensor_R_max);
  
  if (sensor_R_max_state > 128)
  {
    Serial.println("Beginning homing sequence...");
    start_R = millis();
    while (sensor_R_min_state < 256)
    {
      digitalWrite(step_R, HIGH);
      delayMicroseconds(250);
      digitalWrite(step_R, LOW);
      delayMicroseconds(250);
      sensor_R_min_state = analogRead(sensor_R_min);
    }
  }
  // Calculate and print 
  stop_R = millis();
  time_R = stop_R - start_R;
  Serial.print("Homed to minimum in ");
  Serial.print(time_R);
  Serial.println(" ms");
  digitalWrite(direction_R, HIGH);

  // counting test
  for (int i=2; i >= 0; i--)
  {
    for (int j=9; j >= 0; j--)
    {
      unsigned long startTime = millis();
      for (unsigned long elapsed=0; elapsed < 333; elapsed = millis() - startTime)
      {
        lightSegments(numbers[j], ones);
        lightSegments(numbers[i], tens);
      }    
    }
  }

  while (!button.isPressed())
    button.loop();
    Serial.println("Button was pressed; starting program.");
}

void loop()
{
  start_R = millis();
  sensor_R_max_state = analogRead(sensor_R_max);
  while (sensor_R_max_state < 256)
  {
    sensor_R_max_state = analogRead(sensor_R_max);
    digitalWrite(step_R, HIGH);
    delayMicroseconds(1000);
    digitalWrite(step_R, LOW);
    delayMicroseconds(1000);
  }
  
  // FIXME: This repeats continuously so only first output is accurate
  stop_R = millis();
  time_R = stop_R - start_R;
  Serial.print("Hit maximum in ");
  Serial.print(time_R);
  Serial.println(" ms");
}

void lightSegments(byte number, const int digit[])
{
  //Serial.print("bit: ");
  for (int i = 0; i < 4; i++)
  {
    int bit = bitRead(number, i);
    digitalWrite(digit[i], bit);
    //Serial.print(bit);
  }
  //Serial.println();
}

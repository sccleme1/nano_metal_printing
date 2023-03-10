/*Example sketch to control a stepper motor with A4988 stepper motor driver and Arduino without a library. More info: https://www.makerguides.com */

// Define stepper motor connections and steps per revolution:
//#define direction_L 2
//#define step_L 3
#define direction_R 4
#define step_R 5

#define sensor_R_min A0
#define sensor_R_max A1
//#define sensor_L_min A2
//#define sensor_L_max A3

#define stepsPerRevolution 200

int sensor_R_min_state = 0;  //
int sensor_R_max_state = 0;
//int sensor_L_min_state = 0;         // variable for reading the pushbutton status
//int sensor_L_max_state = 0;

void setup() {
  // Declare pins as output:
  pinMode(direction_R, OUTPUT);
  pinMode(step_R, OUTPUT);
  //pinMode(direction_L, OUTPUT);
  //pinMode(step_L, OUTPUT);
  
  pinMode(sensor_R_min, INPUT);
  pinMode(sensor_R_max, INPUT);
  //pinMode(sensor_L_min, INPUT);
  //pinMode(sensor_L_max, INPUT);

  Serial.begin(9600);

  Serial.println("Beginning serial...");

  digitalWrite(direction_R, HIGH);
}

void loop()
{
  sensor_R_max_state = analogRead(sensor_R_max);
  sensor_R_min_state = analogRead(sensor_R_min);
  if (sensor_R_max_state > 128)
  {
    Serial.println("hit MAX");
    digitalWrite(direction_R, LOW);
  }
  else if (sensor_R_min_state > 128)
  {
    Serial.println("hit MIN");
    digitalWrite(direction_R, HIGH);
  }
  
  //delay(10);
 
  Serial.println("moving..."); 
  // These four lines result in 1 step:
  digitalWrite(step_R, HIGH);
  delayMicroseconds(1000);
  digitalWrite(step_R, LOW);
  delayMicroseconds(1000);
  digitalWrite(step_R, HIGH);
  delayMicroseconds(1000);
  digitalWrite(step_R, LOW);
  delayMicroseconds(1000);
}

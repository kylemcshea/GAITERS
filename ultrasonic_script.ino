//Ultrasonic Sensor #1
const int trigPin[] = {2,4,6,8,10,12}; // Trigger Pin of Ultrasonic Sensor(s)
const int echoPin[] = {3,5,7,9,11,13}; // Echo Pin of Ultrasonic Sensor(s)

//blue->white->yellow->orange->yell/orng->blue/black
//indicate # of sensors
const int numberOfSensors = 6;

int counter = 0;
int base[numberOfSensors];

float distance[numberOfSensors];
float distancePrev[numberOfSensors];

void setup() {
  for (int i =0;i<numberOfSensors;i++){
    pinMode(trigPin[i],OUTPUT);
    pinMode(echoPin[i],INPUT);
  }
  Serial.begin(9600); // Starting Serial Terminal
}
int getDistance(int trigPin, int echoPin){
  float duration, distanceTemp;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceTemp = (duration*.0343)/2;
  return distanceTemp;
}
void loop() {

  //Ultrasonic Sensor 1 functions
  for(int i = 0; i < numberOfSensors; i++){
    distancePrev[i] =distance[i];
    distance[i] = getDistance(trigPin[i], echoPin[i]);
    if(counter > 100){
      if(distance[i] > 1.5*base[i]){
        distance[i] = distancePrev[i];
        Serial.print("Reseting to previous distance at sensor " + String(i));
      }
    }
    if(counter < 100){
      base[i]+= distance[i];
    }
    if(counter == 100){
      base[i]/=100;
      Serial.println("BASE " + String(i) + " = " + String(base[i]));
      delay(2000);
    }
  }
  Serial.print("["+String(counter)+"] ");
  for(int j = 0; j < numberOfSensors; j++){
    Serial.print("Sensor " + String(j) + ": " + String(distance[j]) + " | ");
  }
  Serial.println();
   
  counter++;
  delay(200);
}

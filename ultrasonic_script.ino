//Ultrasonic Sensor #1
const int trigPin[] = {7, 13}; // Trigger Pin of Ultrasonic Sensor(s)
const int echoPin[] = {6, 12}; // Echo Pin of Ultrasonic Sensor(s)

//indicate # of sensors
const int numberOfSensors = 2;

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
    if(counter > 20){
      if(distance[i] > 1.5*base[i]){
        distance[i] = distancePrev[i];
        Serial.print("Reseting to previous distance at sensor " + String(i));
      }
    }
    if(counter < 20){
      base[i]+= distance[i];
    }
    if(counter == 20){
      base[i]/=20;
      Serial.println("BASE " + String(i) + " = " + String(base[i]));
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

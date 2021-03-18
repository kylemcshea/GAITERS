//import processing.serial;
//Table dataTable; //Table we use for csv
//int numReadings = 500; //number of readings taken before publishing data.

//String fileName;

//TODO => Set up VS code on computer
//TODO => Make it so that echoPin / TrigPin iterate odds/evens

const int echoPin[] = {52,50,48,46,44,42,40,38,36,34,32,30,28,26,24,22}; // Trigger Pin of Ultrasonic Sensor(s)
const int trigPin[] = {53,51,49,47,45,43,41,39,37,35,33,31,29,27,25,23}; // Echo Pin of Ultrasonic Sensor(s)

//blue->white->yellow->orange->yell/orng->blue/black
//indicate # of sensors
const int numberOfSensors = 16;
const int buttonPin = 7;

int counter = 0;
int base[numberOfSensors];
int buttonState;

int distance[numberOfSensors];
//float distancePrev[numberOfSensors];

void setup() {
  //table.addColumn("Count");
  for (int i =0;i<numberOfSensors;i++){
    pinMode(trigPin[i],OUTPUT);
    pinMode(echoPin[i],INPUT);
    //table.addColumn("Sensor ["+String(i)+"]");
  }
  pinMode(buttonPin, INPUT);
  digitalWrite(buttonPin, HIGH);
  Serial.begin(9600); // Starting Serial Terminal
}
//Grabs distance from sensor reading
int getDistance(int trigPin, int echoPin){
  int duration, distanceTemp;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distanceTemp = (duration*.0343)/2;
  return distanceTemp;
}
//TODO => Figure out what the best delay time is to create "perfect" readings
void loop() {
  //Ultrasonic Sensor functions
  //TableRow newRow = dataTable.addRow(); //Create row for input 
  //newRow.setInt("Count",counter); //Indicates what count readings are for in csv
  for(int i = 0; i < numberOfSensors; i++){ //Grabs distance from each sensor
    //saves distance previous as fallback in case this reading is noisey
    //can definitely do this better, should use something like distance[i-1]
    //distancePrev[i] =distance[i];
    distance[i] = getDistance(trigPin[i], echoPin[i]);
    //TODO => Set a thresh hold for how many counts we want to set as baseline
    //if(counter > 100){
      //if(distance[i] > 1.5*base[i]){
        //distance[i] = distancePrev[i];
        //Serial.print("Reseting to previous distance at sensor " + String(i));
      //}
    //}
    //newRow.setInt("Sensor ["+String(i)+"]",distance[i]);
    
    //TODO => make sure this 100 as well is modularized in threshold
    if(counter < 100){
      base[i]+= distance[i];
    }
    //TODO => Same with this one
    //if(counter == 100){
      //base[i]/=100;
      //Serial.println("BASE " + String(i) + " = " + String(base[i]));
      //delay(2000);
    //}
  }
  buttonState = digitalRead(buttonPin);
  Serial.print(String(counter)+"| ");
  for(int j = 0; j < numberOfSensors; j++){
    Serial.print("Sensor " + String(j) + ": " + String(distance[j]) + " | ");
  }
  if(buttonState == HIGH){
    Serial.print("Output: 0|");
  }
  else{
    Serial.print("Output: 1|");
  }
  
  Serial.println();
  //if(Counter%numReadings == 0){
    //fileName = String(year())+ String(month())+String(day()) + String(Counter/numReadings);
    //saveTable(dataTable,fileName);
  //}
  counter++;
  //TODO => Need to find the right delay time. Set as variable so its easy to test.
  delay(1000);
}

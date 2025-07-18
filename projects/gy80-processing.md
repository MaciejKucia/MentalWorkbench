# Processing GUI

## Plotting sensors data

  * Compiled in Processing 2.0b6
  * <https://www.processing.org>

```java
// Created 4.11.12
// by Maciej Kucia

import processing.serial.*;

Serial myPort;        // The serial port
int xPos = 1;         // horizontal position of the graph

// 0 - old 1-new 2-max
float [][] values = new float[11][3];

color[] colors = {color(255,0,0),color(0,255,0),color(0,0,255),color(255,255,0),color(0,255,255),color(255,0,255),color(100,100,0),color(100,0,100),color(0,100,100),color(20,50,80),color(80,50,20)}; 
boolean[] offChannel = {true,true,true,false,false,false,false,false,false,false,false};

void cleanup()
{
  background(255,255,255);
  stroke(0);
  line(0, height/2 , width, height/2);
  xPos = 0;
}

void setup () 
{
  // set the window size:
  size(800, 600);        

  println(Serial.list());
  myPort = new Serial(this, Serial.list()[1], 115200);
  //                                      ^ UPDATE THIS MANUALLY!
  // don't generate a serialEvent() unless you get a newline character:
  myPort.bufferUntil('\n');
  cleanup();
}

void keyPressed() 
{
  switch (key)
  {
    case '1': offChannel[0] = !offChannel[0]; break;
    case '2': offChannel[1] = !offChannel[1]; break;
    case '3': offChannel[2] = !offChannel[2]; break;
    case '4': offChannel[3] = !offChannel[3]; break;
    case '5': offChannel[4] = !offChannel[4]; break;
    case '6': offChannel[5] = !offChannel[5]; break;
    case '7': offChannel[6] = !offChannel[6]; break;
    case '8': offChannel[7] = !offChannel[7]; break;
    case '9': offChannel[8] = !offChannel[8]; break;
    case '0': offChannel[9] = !offChannel[9]; break;
    case '-': offChannel[10] = !offChannel[10]; break;
    case 'c': cleanup(); break;
    default: println("key not active");
  }
}

void serialEvent (Serial myPort) {
  // get the ASCII string:
  String inString = myPort.readStringUntil('\n');

  if (inString == null) return;
  
   //println(inString);
  if (inString.charAt(0) != '~')
  {
    println("No data.");
    return;
  }
  
    // trim off any whitespace:
    inString = trim(inString);

    String[] inStrings = inString.split(",");
    
    for(int i=0;i<=10;++i)
    {
      values[i][0] = values[i][1];
      values[i][1] = float(inStrings[i+1]);
      
      //store max
      if (values[i][1] > values[i][2])
        values[i][2] = values[i][1];
      
      values[i][1] = map(values[i][1], -values[i][2], values[i][2], 0, height);
    }

    // draw the line:
    for(int i=0;i<=10;++i)
    {
     if (!offChannel[i]) continue;
     stroke(colors[i]);
     line(xPos, values[i][0], xPos+1, values[i][1]);
    }
    
    // at the edge of the screen, go back to the beginning:
    if (xPos++ >= width) 
    {
      cleanup();
    } 
  
}


void draw () {
  // everything happens in the serialEvent()
}

```

## Kalman

```c
// Created 4.11.12
// by Maciej Kucia

import processing.serial.*;

Serial myPort;        // The serial port
int xPos = 1;         // horizontal position of the graph

// 0 - old
// 1 - new 
// 2 - scale
float [][] values = new float[11][3];
float kalman_old = 0;

// sensor data to be filtered
int kalman_sensor = 5;

color[] colors = {
  color(255, 0, 0), color(0, 255, 0), color(0, 0, 255), color(255, 255, 0), color(0, 255, 255), color(255, 0, 255), color(100, 100, 0), color(100, 0, 100), color(0, 100, 100), color(20, 50, 80), color(80, 50, 20),color(0,0,0)}; 

boolean[] offChannel = {
  false, true, false, false, false, false, false, false, false, false, false};

boolean enableKalman = true;
boolean enableMeasurement = true;

class KalmanFilterC
{
  // kalman variables
  public double q; // process noise
  public double r; // measurement noise
  public double x; // value
  public double p; // estimation error covariance
  public double k; // kalman gain
  
  public double scale;

  public KalmanFilterC()
  {
    x = 0;
    q = 100;
    r = 10000;
    p = 10000;
    k = 0;
    
    //for plotting
    scale = 0.01;
  }

  void Update(double x_m)
  {
    p = p + q; // we have more noise
    
    k = p / (p+r);
    
    // update by error* kalman gain
    x = x + k * (x_m - x);
    p = (1-k)*(1-k)* p + r*k*k;
  }
  
  void Print()
  {
    println(" q r p k x[" + q +":"+ r +":"+ p +":"+ k +":"+ x + "]");
  }
  
}

KalmanFilterC kalman;

// code

void cleanup()
{
  background(255, 255, 255);
  stroke(0);
  line(0, height/2, width, height/2);
  xPos = 0;
}

void setup () 
{
  // set the window size:
  size(800, 600);        

  kalman = new KalmanFilterC();

  //for(int i=0;i<values[0].length;++i)
  values[kalman_sensor][2] = (float)kalman.scale;

  println(Serial.list());
  myPort = new Serial(this, Serial.list()[1], 115200);
  //                                      ^ UPDATE THIS MANUALLY!
  
  // don't generate a serialEvent() unless you get a newline character:
  myPort.bufferUntil('\n');
  cleanup();
}

void keyPressed() 
{
  switch (key)
  {
  case 'm':
    enableMeasurement = !enableMeasurement;
    break;
    
  case 'c': 
    cleanup(); 
    break;
    
  case 'k': 
    enableKalman = !enableKalman;
    break;
    
  default: 
    println("key not active");
  }
}

void Process()
{
  if (enableKalman)
    kalman.Update(values[kalman_sensor][1]);
}

void Plot()
{
   if (enableMeasurement)
   {
    stroke(colors[colors.length-1]);
    line(xPos, values[kalman_sensor][0]*values[kalman_sensor][2]+(height/2), xPos+1, values[kalman_sensor][1]*values[kalman_sensor][2]+(height/2));
   }
  
  if(enableKalman)
  {
   float new_kalman = (float)kalman.x; 
   
   stroke(color(255, 0, 0,200));
   line(xPos, (float)(kalman_old * kalman.scale)+(height/2), xPos+1,(float)(new_kalman * kalman.scale)+(height/2));
   kalman_old = new_kalman;
   //kalman.Print();
  }

  // at the edge of the screen, go back to the beginning:
  if (xPos++ >= width) 
    cleanup();
 
}

void serialEvent (Serial myPort) {
  // get the ASCII string:
  String inString = myPort.readStringUntil('\n');

  if (inString == null) return;

  //println(inString);
  if (inString.charAt(0) != '~')
  {
    println("No data.");
    return;
  }

  // trim off any whitespace:
  inString = trim(inString);

  String[] inStrings = inString.split(",");

  for (int i=0;i<=10;++i)
  {
    values[i][0] = values[i][1];
    values[i][1] = float(inStrings[i+1]);
  }
  
  Process();
  Plot();

}


void draw () {
  // everything happens in the serialEvent()
}

```

## Complementary filter

```c
// Created 1.12.12
// by Maciej Kucia

import processing.serial.*;

Serial myPort;        // The serial port
int xPos = 1;         // horizontal position of the graph

color[] colors = {
  color(255, 0, 0), color(0, 255, 0), color(0, 0, 255), color(255, 255, 0), color(0, 255, 255), color(255, 0, 255), color(100, 100, 0), color(100, 0, 100), color(0, 100, 100), color(20, 50, 80), color(80, 50, 20), color(0, 0, 0)
}; 

// Timestep
float deltaT = (1/50);

class SensorsC
{
  public float gyroX=0;
  public float gyroY=0;
  public float gyroZ=0;

  public float accX=0;
  public float accY=0;
  public float accZ=0;

  public float gyroAngle=0;
  public float accAngle=0;

  public float Angle =0.0;

  public void UpdateMeasurements(float gX, float gY, float gZ, float aX, float aY, float aZ)
  {
    // 250 dps
    // 25Hz = 40ms
    gyroX=(0.04*gX)/250.0;
    gyroY=(0.04*gY)/250.0;
    gyroZ=(0.04*gZ)/250.0;

    // range +-4g - 11 bits = 10 bits + sign
    // (2^10)-1 = 4g -> 4g = 1023 -> 1g = 255 
    accX=aX/255.0;
    accY=aY/255.0;
    accZ=aZ/255.0;

    accAngle = (float)Math.toDegrees(Math.atan2(aZ, aX) + Math.PI*0.5 );

    // "fuse" two sensor data
    Angle =  (0.90)*(Angle+gyroY) + (0.10)*accAngle;
  }

  public void Draw()
  {
    //DrawAcc();
    //DrawGyroAngle();
    //DrawAccAngle();
    DrawComplAngle();
  }

  public void DrawAcc()
  {
    float hh = ((float)height/2.0);
    stroke(color(0, 255, 0, 100));

    //blue
    stroke(color(0, 0, 255, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-accX*90) );

    //green
    stroke(color(0, 255, 0, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-accY*90) );

    //red
    stroke(color(255, 0, 0, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-accZ*90) );
  }

  public void DrawGyro()
  {
    float hh = ((float)height/2.0);
    stroke(color(0, 255, 0, 100));

    //blue
    stroke(color(0, 0, 255, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-gyroX) );

    //green
    stroke(color(0, 255, 0, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-gyroY) );

    //red
    stroke(color(255, 0, 0, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-gyroZ) );
  }

  public void DrawGyroAngle()
  {
    float hh = ((float)height/2.0);
    stroke(color(0, 255, 0, 100));

    //blue
    stroke(color(0, 0, 255, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-gyroAngle) );
  }

  public void DrawAccAngle()
  {
    float hh = ((float)height/2.0);
    stroke(color(0, 255, 0, 100));

    //red
    stroke(color(255, 0, 0, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-accAngle) );
  }


  public void DrawComplAngle()
  {
    float hh = ((float)height/2.0);
    stroke(color(0, 255, 0, 100));

    //green
    stroke(color(0, 255, 0, 100));
    line((float)xPos, hh, (float)xPos, (float) (hh-Angle) );
  }
}

SensorsC sensors = new SensorsC();

void cleanup()
{
  float hh = ((float)height/2.0);
  background(255, 255, 255);
  stroke(0);
  line(0, hh, width, hh);
  stroke(100, 100, 100);
  line(0, hh-90, width, hh-90);
  line(0, hh+90, width, hh+90);

  xPos = 0;
}

void setup () 
{
  // set the window size:
  size(800, 400);        

  println(Serial.list());
  myPort = new Serial(this, Serial.list()[1], 115200);
  //                                      ^ UPDATE THIS MANUALLY!

  // don't generate a serialEvent() unless you get a newline character:
  myPort.bufferUntil('\n');

  myPort.clear();
  cleanup();
}

void keyPressed() 
{
  switch (key)
  {

  case 'c': 
    cleanup(); 
    break;

  default: 
    println("key not active");
  }
}

void serialEvent (Serial myPort) {

  String inString = myPort.readStringUntil('\n');

  if (inString == null) return;
  if (inString.charAt(0) != '~')
  {
    println("No data.");
    return;
  }

  String[] inStrings = trim(inString).split(",");

  sensors.UpdateMeasurements(
  float(inStrings[4]), float(inStrings[5]), float(inStrings[6]), 
  float(inStrings[1]), float(inStrings[2]), float(inStrings[3]));

  sensors.Draw();

  // at the edge of the screen, go back to the beginning:
  if (xPos++ >= width) 
    cleanup();
}


void draw () {
  // everything happens in the serialEvent()
}

```

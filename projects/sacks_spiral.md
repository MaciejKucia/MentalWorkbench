# Sacks spiral in Processing

```
int i=0;
int centerx,centery;

void setup()
{
  size(500,500);
  frameRate(1000);
  centerx = width/2;
  centery = height/2;
  ellipseMode(CENTER);
  rectMode(CENTER);
  background(255);
}

boolean isprime(int n)
{
    if (n%2==0) return false;
    for(int i=3; i*i <= n; i+=2) 
        if(n%i==0) return false;
    return true;
}

void draw()
{
  if (isprime(i++))
  {
    fill(0);
  
    float r = sqrt(i-1);
    float X = centerx + (r*cos(radians(360*r)))*1;
    float Y = centery + (r*sin(radians(360*r)))*1;
    //ellipse(X,Y,4,4);
    rect(X,Y,1,1);
  }
}
```

![alt](/projects/sacks_spiral.png)

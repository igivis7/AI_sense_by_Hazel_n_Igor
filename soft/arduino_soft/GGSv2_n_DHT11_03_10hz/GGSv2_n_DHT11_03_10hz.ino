//=================
// setup for GGSv2
//=================
#include "Multichannel_Gas_GMXXX.h"

#ifdef SOFTWAREWIRE
    #include <SoftwareWire.h>
    SoftwareWire myWire(3, 2);
    GAS_GMXXX<SoftwareWire> gas;
#else
    #include <Wire.h>
    GAS_GMXXX<TwoWire> gas;
#endif

static uint8_t recv_cmd[8] = {};

//================
// setup for DHT11
//================
#include "dht.h"
dht DHT;
#define DHT11_PIN 2

float temperature_c;
float temperature_g = 0.0;
float humidity_c;
float humidity_g = 0.0;

int temperature_g_int;
int humidity_g_int;

//================
// setup general
//================
#include <math.h>
// (int)floorf(x + 0.5f);
void setup() {
  Serial.begin(9600);
  gas.begin(Wire, 0x08); // use the hardware I2C
}



//===================================================================
//===================================================================
//===================================================================
//===================================================================



void loop( )
{
  uint32_t valGM102B = 0;
  uint32_t valGM302B = 0;
  uint32_t valGM502B = 0;
  uint32_t valGM702B = 0;


  // updates values of DHT11 reading only when they are correct (not -999)
  int chk = DHT.read11(DHT11_PIN);
  temperature_c = DHT.temperature;
  humidity_c = DHT.humidity;
  if ((temperature_c >= 0) && (temperature_c < 100) && (humidity_c >= 0) && (humidity_c < 110) )
  {
    temperature_g = temperature_c;
    humidity_g = humidity_c;
  }



  valGM102B = gas.getGM102B(); 
  Serial.print(valGM102B); 
  Serial.print(","); 

  valGM302B = gas.getGM302B(); 
  Serial.print(valGM302B); 
  Serial.print(",");

  valGM502B = gas.getGM502B(); 
  Serial.print(valGM502B); 
  Serial.print(",");

  valGM702B = gas.getGM702B(); 
  Serial.print(valGM702B);
  Serial.print(",");

  temperature_g_int = temperature_g;
  humidity_g_int = humidity_g;
  Serial.print(temperature_g_int);
  Serial.print(",");
  Serial.println(humidity_g_int);
  
  delay(100);
}




//===================================================================
//===================================================================
//===================================================================
//===================================================================

#include <ESP8266WiFi.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
TinyGPSPlus gps;
SoftwareSerial ss(4, 5);

float latitude;
float longitude;
const char* ssid     = "Vins";
const char* password = "hello123";
const char* host = "pettttttrack.000webhostapp.com";

void setup(){
  ss.begin(9600);
  
  WiFi.begin(ssid, password); 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  } 
}

void loop(){
  while (ss.available() > 0){
    if(gps.encode(ss.read())){
      if(gps.location.isValid()){
          latitude=gps.location.lat();
          longitude=gps.location.lng();
  }
    }
  }
  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(host, httpPort)) {
    return;
  }
  String url = "/api/insert.php?latitude=" + String(latitude) + "&longitude="+ String(longitude);
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  delay(500);
  while(client.available()){
    String line = client.readStringUntil('\r');
  }
  delay(6000);
}

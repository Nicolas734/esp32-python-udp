#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "";          //  Coloque o nome do wifi
const char* password = "";      //  Coloque a senha do wifi
const char* server_ip = "";     //  Coloque o endereço IP do servidor Python
const int server_port = 0000;   //  Coloque a porta do servidor Python

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.print("Conectando");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Conectado ao WiFi");
}

void loop() {
  String message = "Hello from ESP32!";
  
  udp.beginPacket(server_ip, server_port);
  udp.print(message);
  udp.endPacket();
  
  Serial.println("Mensagem enviada ao servidor: " + message);
  
  delay(5000);
}

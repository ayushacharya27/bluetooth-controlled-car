#include <ESP8266WiFi.h>
const int for1 = 0;
const int rev1 = 1;
const int for2 = 2;
const int rev2 = 3;
void left() {
  digitalWrite(for1, HIGH);
  digitalWrite(rev2, HIGH);
  digitalWrite(for2, LOW);
  digitalWrite(rev1, LOW);
}

void right() {
  digitalWrite(for2, HIGH);
  digitalWrite(rev1, HIGH);
  digitalWrite(for1, LOW);
  digitalWrite(rev2, LOW);
}

void reverse() {
  digitalWrite(rev1, HIGH);
  digitalWrite(rev2, HIGH);
  digitalWrite(for1, LOW);
  digitalWrite(for2, LOW);
}

void straight() {
  digitalWrite(for1, HIGH);
  digitalWrite(for2, HIGH);
  digitalWrite(rev1, LOW);
  digitalWrite(rev2, LOW);
}

void stop() {
  digitalWrite(for1, LOW);
  digitalWrite(for2, LOW);
  digitalWrite(rev1, LOW);
  digitalWrite(rev2, LOW);
}

bool forward_moving_flag = false;
bool stop_flag = false;
bool reverse_moving_flag = false;
bool left_moving_flag = false;
bool right_moving_flag = false;


const char* ssid = "1";
const char* password = "madarchod";
WiFiServer server(80);

void setup() {
  pinMode(for1, OUTPUT);
  pinMode(rev1, OUTPUT);
  pinMode(for2, OUTPUT);
  pinMode(rev2, OUTPUT);
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("Connected to Wi-Fi");
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New client connected");
    String request = "";

    while (client.available()) {
      char c = client.read();
      request += c;
      delay(1);
    }

    Serial.println("Received request:");
    Serial.println(request);

    // Extract command from the request
    String command = "";
    int commandIndex = request.indexOf("command=");
    if (commandIndex != -1) {
      commandIndex += 8; // length of "command="
      int endIndex = request.indexOf(' ', commandIndex);
      if (endIndex == -1) {
        endIndex = request.length();
      }
      command = request.substring(commandIndex, endIndex);
    }

    Serial.print("Extracted command: ");
    Serial.println(command);

    // Process the command
    if (command == "n") {
      right_moving_flag = false;
      stop_flag = true;
      reverse_moving_flag = false;
      forward_moving_flag = false;
      left_moving_flag = false;
       
      
    } else if (command == "s") {
      right_moving_flag = false;
      stop_flag = false;
      reverse_moving_flag = true;
      forward_moving_flag = false;
      left_moving_flag = false;
    } else if (command == "a") {
      right_moving_flag = false;
      stop_flag = false;
      reverse_moving_flag = false;
      forward_moving_flag = false;
      left_moving_flag = true;
    } else if (command == "d") {
      right_moving_flag = true;
      stop_flag = false;
      reverse_moving_flag = false;
      forward_moving_flag = false;
      left_moving_flag = false;
    } else if (command == "w") {
      right_moving_flag = false;
      stop_flag = false;
      reverse_moving_flag = false;
      forward_moving_flag = true;
      left_moving_flag = false;
    }
    if(forward_moving_flag && !stop_flag && !reverse_moving_flag && !left_moving_flag && !right_moving_flag){
      straight();
    }
    else if(!forward_moving_flag && stop_flag && !reverse_moving_flag && !left_moving_flag && !right_moving_flag){
      stop();
    }
    else if(!forward_moving_flag && !stop_flag && reverse_moving_flag && !left_moving_flag && !right_moving_flag){
      reverse();
    }
    else if(!forward_moving_flag && !stop_flag && !reverse_moving_flag && left_moving_flag && !right_moving_flag){
      left();
    }
    else if(!forward_moving_flag && !stop_flag && !reverse_moving_flag && !left_moving_flag && right_moving_flag){
      right();
    }

    // Send HTTP response
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/plain");
    client.println("Connection: close");
    client.println();
    client.println("Command received");

    client.stop();
  }
}

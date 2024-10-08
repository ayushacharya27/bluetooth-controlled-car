const int for1 = 7;
const int rev1 = 6;
const int for2 = 12;
const int rev2 = 4;

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
void setup(){
  Serial.begin(9600);
  pinMode(for1, OUTPUT);
  pinMode(rev1, OUTPUT);
  pinMode(for2, OUTPUT);
  pinMode(rev2, OUTPUT);
}

void loop(){
  if(Serial.available()){
    char command = Serial.read();

    if(command == 'w'){
      right_moving_flag = false;
      stop_flag = false;
      reverse_moving_flag = false;
      forward_moving_flag = true;
      left_moving_flag = false;
    }
    else if(command == 'a'){
      right_moving_flag = false;
      stop_flag = false;
      reverse_moving_flag = false;
      forward_moving_flag = false;
      left_moving_flag = true;
    }
    else if(command == 's'){
      right_moving_flag = false;
      stop_flag = false;
      reverse_moving_flag = true;
      forward_moving_flag = false;
      left_moving_flag = false;
    }
    else if(command == 'n'){
      right_moving_flag = false;
      stop_flag = true;
      reverse_moving_flag = false;
      forward_moving_flag = false;
      left_moving_flag = false;
    }
    else if(command = 'd'){
      right_moving_flag = true;
      stop_flag = false;
      reverse_moving_flag = false;
      forward_moving_flag = false;
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
  }
}

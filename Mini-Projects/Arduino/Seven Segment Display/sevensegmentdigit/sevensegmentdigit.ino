//######################################
// ______     _____                                 _    ___  ___          _        __    ____   _____                   _            
//|___  /    /  ___|                               | |   |  \/  |         | |      /  |  / ___| /  __ \                 | |           
//   / /_____\ `--.  ___  __ _ _ __ ___   ___ _ __ | |_  | .  . | ___   __| |______`| | / /___  | /  \/ ___  _   _ _ __ | |_ ___ _ __ 
//  / /______|`--. \/ _ \/ _` | '_ ` _ \ / _ \ '_ \| __| | |\/| |/ _ \ / _` |______|| | | ___ \ | |    / _ \| | | | '_ \| __/ _ \ '__|
//./ /       /\__/ /  __/ (_| | | | | | |  __/ | | | |_  | |  | | (_) | (_| |      _| |_| \_/ | | \__/\ (_) | |_| | | | | ||  __/ |   
//\_/        \____/ \___|\__, |_| |_| |_|\___|_| |_|\__| \_|  |_/\___/ \__,_|      \___/\_____/  \____/\___/ \__,_|_| |_|\__\___|_|   
//                        __/ |                                                 ~7-Segment Mod-16 Counter with Interrupt Handling~                                                                                 
//                       |___/                                                   by joshuqa aka Roni                                                                                                                                                                                                               
//                                                                               
// GitHub: https://github.com/nobalpha
//######################################

// Creating an bit wised alphabet for base 16 representation in 7-segment display.
int alphabet[16] = {0b0111111, 0b0000110, 0b1011011, 0b1001111, 0b1100110, 0b1101101, 0b1111101, 0b0000111, 0b11111111, \
0b1101111, 0b1110111, 0b1111100, 0b0111001, 0b1011110, 0b1111001, 0b1110001};


int interrupter = 2; // Interrupter pin [Arduino UNO: 2, 3]
int control = 6; // Logically circuit starter pin
int updater = 5; // Digit updater pin
int initd = 0; // Starting number
bool fired = false; // Boolean started value

void setup() {
  for (int i = 7; i < 14; i++) // Automatically modding pin numbers.
    pinMode(i, OUTPUT);
  pinMode(interrupter, INPUT);
  pinMode(control, INPUT);
  pinMode(updater, INPUT_PULLUP);
  attachInterrupt(interrupter, reset, CHANGE); // Making a reset-call interrupt to be able to reset initd to 0.
}

void loop() {
  bool fired = digitalRead(control); // Checking the swicth's state.
  if (fired) { // If switch is closed
    showDecimal(initd); // Prints hex format
    bool updated = digitalRead(updater); // Checking the update button.
    if (updated) { // If it gets pressed
      initd = (initd + 1) % 16 ; // Incrementing initd's value by one and getting it's modulo 16 to be able to prevent array overflow.
      updated = false; // Sets back to it's default state.
      delay(300); // Delay to prevent max-overloading (number jumping [0->E])
    }
  } else {
    clear(); // If it's not opened or it's closed, clears the output.
  }

}

void reset() {
  initd = 0; // Resets via interruption.
}


void clear() {
  for (int p = 7; p < 14; p++) // Disables all the ports belonging to 7-segment display.
    digitalWrite(p, 0);
}

void showDecimal(int dec) {
  dec = dec % 16; // Sanitizes input to prevent array overflow.
    int temp = alphabet[dec]; // Gets the equivalant hex number in base 2 (7 bit).
    for (int p = 7; p <= 13; p++) // Loops over the ports
      digitalWrite(p, bitRead(temp, 13-p));   // And reads it's bits [bitRead reads like Little-Endian]. Then, substractes from 13 (max-port), by this way we decrease Big-O complexity without using two variables. 
}
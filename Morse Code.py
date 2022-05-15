import time
from playsound import playsound

translate_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                  'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
                  '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                  " ": "/"}

message = "This is just an example message"
message = " ".join(translate_dict[c] for c in message.upper())

def play_morse_code(message):
    for c in message:
        if c == ".":
            print("Short Sound")
            time.sleep(0.3)
        elif c == "-":
            print("Long Sound")
            time.sleep(0.3)
        elif c == "/" or c == " ":
            time.sleep(0.5)
        else:
            print("Invalid character detected!")

print(message)
play_morse_code(message)


from machine import Pin
from time import sleep

# Pin Setup
ldr_sensor = Pin(4, Pin.IN)

# Morse Code Dictionary
MORSE_CODE_DICTIONARY = { '  ': ' ',
                          'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                          'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                          'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                          'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                          'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                          '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                          '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
                          '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '_': '_',
                          }

def morse_to_text(morse_code):
    """Convert Morse code to text."""
    decoded_text = [char for symbol in morse_code.split() for char, code in MORSE_CODE_DICTIONARY.items() if symbol == code]
    text = ''.join(decoded_text)
    print(f"Decoded Text: {text}")

def read_morse_code():
    """Read Morse code from LDR."""
    pulse_durations = []
    pulse_duration = 0
    pulse_count = 0
    
    while True:
        ldr_value = ldr_sensor.value()
        sleep(0.5)
        
        if ldr_value == 1:
            while ldr_sensor.value() == 1:
                pulse_duration += 1
                sleep(0.1)
                
            pulse_durations.append(pulse_duration)
            pulse_duration = 0
            pulse_count += 1
            
            if pulse_count >= 15:
                break
            
            sleep(0.2)
        else:
            if pulse_count >= 15:
                break

    return pulse_durations

def convert_to_morse_code(pulse_durations):
    """Convert pulse durations to Morse code and decode."""
    pulse_string = ''.join(str(duration) for duration in pulse_durations)
    print(f"Raw Pulse Durations: {pulse_string}")
    
    # Convert pulse durations to Morse code symbols
    morse_code = (pulse_string
                  .replace('000000', ' _ ')  # Word space
                  .replace('00', ' ')        # Letter space
                  .replace('3', '.')         # Dot
                  .replace('4', '.')         # Dot (might need adjustment based on actual timings)
                  .replace('6', '-')         # Dash
                  .replace('7', '-'))       # Dash (might need adjustment based on actual timings)
    
    print(f"Morse Code: {morse_code}")
    morse_to_text(morse_code)

# Main execution
pulse_durations = read_morse_code()
convert_to_morse_code(pulse_durations)

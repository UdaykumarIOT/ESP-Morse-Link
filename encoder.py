from time import sleep
import sys
from machine import Pin
import usocket as socket
import network

# Morse Code Dictionary
MORSE_CODE_DICTIONARY = { ' ': ' ',
                          'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                          'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                          'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                          'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                          'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                          '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                          '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                          '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}

# LED Pin Setup
led = Pin(18, Pin.OUT)
led.off()

# HTML Content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Morse Code Encoder</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <style>
        body {background-color:black;}
        h2 {color:aqua;}
        button {background-color: aqua;}
        input {background-color: aliceblue;
               color:rgb(0, 0, 0);
               font-size:medium;}
    </style>
</head>
<body>
    <br><br><br>
    <center>
        <h2>TEXT A MESSAGE TO SEND</h2>
    </center>
    <center>
        <form>
            <input type="text" name="Text" value="" size="30" autofocus required><br><br>
            <button type="submit">SEND</button>
        </form>
    </center>
</body>
</html>
"""

def enable_hotspot():
    """Enable the hotspot."""
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='MorseCode_AP', password='12345678')
    print("Hotspot enabled, IP address:", ap.ifconfig()[0])

def disable_hotspot():
    """Disable the hotspot."""
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    print("Hotspot disabled")

# Enable Hotspot
enable_hotspot()

def text_to_morse(text):
    """Convert text to Morse code and send to LED."""
    text = text.replace('+', ' ')
    morse_code = ' '.join(MORSE_CODE_DICTIONARY.get(char.upper(), '') for char in text)
    print(f"Original Text: {text}")
    print(f"Morse Code: {morse_code}")
    
    for symbol in morse_code:
        if symbol == '.':
            blink_dot()
        elif symbol == '-':
            blink_dash()
        elif symbol == ' ':
            pause()

def blink_dot():
    """Blink the LED for a dot."""
    led.on()
    sleep(0.3)
    led.off()
    sleep(0.2)

def blink_dash():
    """Blink the LED for a dash."""
    led.on()
    sleep(0.6)
    led.off()
    sleep(0.2)

def pause():
    """Pause for space between Morse code characters."""
    led.off()
    sleep(0.4)

# Create and configure the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 80))
server_socket.listen(5)

while True:
    conn, addr = server_socket.accept()
    request = conn.recv(1024)
    request_str = str(request)
    
    start = request_str.find('=')
    end = request_str.find('HTTP')
    message = request_str[start + 1:end].strip()
    
    if message == 'exit':
        conn.close()
        disable_hotspot()
        sys.exit()

    text_to_morse(message)
    
    response = html_content
    conn.sendall(response)
    conn.close()

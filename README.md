# ESP32-Based Morse Code Transmission and Reception System with Flashlight and LDR Detection

## Overview

This project demonstrates a single-directional Morse code communication system using ESP32 microcontrollers. The system utilizes an LED (flashlight) to transmit Morse code and an LDR (Light Dependent Resistor) to receive and decode the transmitted Morse code. The setup enables wireless communication using simple optical signals.

## Components

- **Transmitter ESP32**:
  - LED connected to GPIO 18
  - Serves a web interface for user input
  - Converts text to Morse code and controls the LED

- **Receiver ESP32**:
  - LDR sensor connected to GPIO 4
  - Detects LED flashes and decodes the Morse code into readable text

## Project Files

- **`encoder.py`**: Manages Morse code encoding and transmission through an LED.
- **`decoder.py`**: Handles the detection and decoding of Morse code using an LDR sensor.

## Features

- **Encoding**: Translates text into Morse code and blinks the LED accordingly.
- **Decoding**: Receives Morse code signals via an LDR and converts them back into text.
- **Web Interface**: Provides a simple form for inputting text to be transmitted (Encoder).
- **Detection and Decoding**: Uses light detection to interpret Morse code (Decoder).

## Setup Instructions

### Transmitter Setup
1. **Hardware**: Connect an LED to GPIO 18 on the first ESP32.
2. **Software**:
   - Upload the `encoder.py` script to the first ESP32.
   - Access the web interface provided by the ESP32 to input text for transmission.

### Receiver Setup
1. **Hardware**: Connect an LDR sensor to GPIO 4 on the second ESP32.
2. **Software**:
   - Upload the `decoder.py` script to the second ESP32.
   - Ensure the LDR is properly positioned to detect the LED flashes from the transmitter.

## Usage

1. **Transmitting Morse Code**:
   - Navigate to the ESP32’s web interface.
   - Enter the text you wish to transmit.
   - The ESP32 will encode the text into Morse code and blink the LED accordingly.

2. **Receiving Morse Code**:
   - The second ESP32, equipped with the LDR sensor, will detect the Morse code signals from the LED.
   - The received Morse code will be decoded and displayed as text in the console.

## Applications

- Educational tool for learning and practicing Morse code.
- Simple optical communication system for scenarios where other communication methods are impractical.
- DIY electronics project for understanding light-based data transmission and reception.

## Documentation

For detailed documentation and additional information, please refer to the [Project Documentation](https://drive.google.com/file/d/1WZoI68UPOLsZ_6QZuQ9HmWHU686xaXf9/view?usp=drive_link).

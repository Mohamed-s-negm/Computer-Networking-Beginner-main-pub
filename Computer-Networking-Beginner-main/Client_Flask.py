import requests
import json
import time
#import RPi.GPIO as GPIO
import random  # Replace with real sensor reading

# Setup LED on Raspberry Pi GPIO pin 18
#LED_PIN = 18
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_PIN, GPIO.OUT)

SERVER_URL = "http://172.21.202.133:5000/light"  # Replace with actual IP

while True:
    # Simulate light sensor reading (Replace with actual sensor code)
    light_level = random.randint(100, 600)  
    print(f"Light Level: {light_level}")

    # Send data to Flask server
    response = requests.post(SERVER_URL, json={"light": light_level})
    response_data = response.json()
    
    if response_data.get("led") == "ON":
        print("Turning ON LED for 1 second...")
        #GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        #GPIO.output(LED_PIN, GPIO.LOW)

    time.sleep(5)  # Wait before next reading

import serial
from ultralytics import YOLO
import time

while True:
    # Initialize serial communication with Arduino
    ser = serial.Serial('COM3', 9600)  # Modify 'COM9' with the appropriate port and 9600 with the baud rate used by your Arduino

    # Initialize YOLO model
    model = YOLO("car_detection_model2.pt")
    results = model.predict("car.jpg")

    # Check if objects are detected
    if len(results) == 0 or len(results[0].boxes) == 0:
        print("No object detected.")
        sig = 0
    else:
        result = results[0]
        box = result.boxes[0]
        class_id = result.names[box.cls[0].item()]
        print("Object type:", class_id)
        sig = 1

    # Send the value of sig to Arduino
    ser.write(bytes(str(sig), 'utf-8'))

    # Close serial communication
    ser.close()

    # Wait for 30 seconds before running the loop again
    time.sleep(20)

import cv2
import numpy as np
import requests
import pyttsx3
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set up female voice
voices = engine.getProperty('voices')
# Try to set female voice - usually index 1 is female voice in Windows
try:
    engine.setProperty('voice', voices[1].id)  # Direct index selection
except:
    # If above fails, try to find by name
    for voice in voices:
        if any(gender in voice.name.lower() for gender in ['female', 'woman', 'girl', 'f']):
            engine.setProperty('voice', voice.id)
            break

# Adjust voice properties
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 1.0)  # Maximum volume

# Initialize API details
API_URL = "https://detect.roboflow.com/driver-fatigue/2"
API_KEY = "7y9E0pW7t5IcONqrvdVn"  # Replace with a valid API key

# Variables to control alert frequency
last_alert_time = 0
ALERT_COOLDOWN = 10  # Minimum seconds between alerts

def speak_alert(message):
    """Speak the alert message using text-to-speech"""
    engine.say(message)
    engine.runAndWait()

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Encode frame as a JPEG image for API request
    _, encoded_image = cv2.imencode(".jpg", frame)
    image_bytes = encoded_image.tobytes()

    # Make API request
    try:
        response = requests.post(
            f"{API_URL}?api_key={API_KEY}",
            files={"file": image_bytes}
        )
        result = response.json()
        print("Predictions:", result)

        # Draw bounding boxes on detected objects
        if "predictions" in result:
            current_time = time.time()
            for obj in result["predictions"]:
                x, y, width, height = int(obj["x"]), int(obj["y"]), int(obj["width"]), int(obj["height"])
                class_name = obj["class"]
                confidence = obj["confidence"]

                # Draw bounding box and label
                start_point = (x - width // 2, y - height // 2)
                end_point = (x + width // 2, y + height // 2)
                
                # Set color based on state (red for fatigue/drowsy, green for awake)
                if class_name.lower() in ['drowsy', 'fatigue', 'tired', 'sleepy']:
                    color = (0, 0, 255)  # Red
                    # Check if enough time has passed since last alert
                    if current_time - last_alert_time >= ALERT_COOLDOWN:
                        speak_alert("Alert! You seem tired. Please take a break and freshen up for your safety.")
                        last_alert_time = current_time
                else:
                    color = (0, 255, 0)  # Green

                cv2.rectangle(frame, start_point, end_point, color, 2)
                cv2.putText(frame, f"{class_name} ({confidence:.2f})", (x - 50, y - 50),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    except Exception as e:
        print(f"Error during inference: {e}")

    # Display the frame
    cv2.imshow("Rider Fatigue Detection", frame)

    # Break on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
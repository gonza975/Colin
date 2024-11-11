import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for Channel A and Channel B
channel_A = 17  # GPIO 17
channel_B = 27  # GPIO 27

# Set up the encoder pins as input and enable internal pull-up resistors
GPIO.setup(channel_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(channel_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize variables
position = 0  # To track the position
last_A = GPIO.input(channel_A)
last_B = GPIO.input(channel_B)

# Define the callback function for edge detection on Channel A
def encoder_callback(channel):
    global position, last_A, last_B
    
    # Read both channels
    A = GPIO.input(channel_A)
    B = GPIO.input(channel_B)

    # Determine direction based on the state change of A and B
    if A == last_A and B != last_B:
        if B == 0:
            position += 1  # Clockwise rotation
        else:
            position -= 1  # Counter-clockwise rotation

    # Update the last state
    last_A = A
    last_B = B

    print(f"Position: {position}")

# Add event detection for both rising and falling edges on Channel A
GPIO.add_event_detect(channel_A, GPIO.BOTH, callback=encoder_callback)

# Run until interrupted
try:
    while True:
        time.sleep(0.01)  # Small delay to reduce CPU usage
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

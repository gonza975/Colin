import RPi.GPIO as GPIO
import time


# GPIO pin setup
channel_a = 17  # GPIO pin for channel A
channel_b = 27  # GPIO pin for channel B

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(channel_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables to store position and direction
position = 0
last_state = GPIO.input(channel_a)

def update_position(channel):
    global position, last_state
    # Read the current states of channel A and B
    current_state = GPIO.input(channel_a)
    b_state = GPIO.input(channel_b)

    # Determine direction based on the change in channel A and state of channel B
    if current_state != last_state:  # State has changed
        if b_state != current_state:
            position += 1  # Clockwise
        else:
            position -= 1  # Counter-clockwise
        last_state = current_state
    print(f"Current position: {position}")

# Attach the event to the channel A pin
GPIO.add_event_detect(channel_a, GPIO.BOTH, callback=update_position)

try:
    print("Starting position tracking...")
    while True:
        time.sleep(0.1)  # Main loop can be adjusted for other tasks

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()

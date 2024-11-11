import RPi.GPIO as GPIO
import time

# Define the GPIO pins for Channel A and Channel B
channel_A = 17  # GPIO 17
channel_B = 27  # GPIO 27

def setup_gpio():
    """Set up GPIO pins and add edge detection."""
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(channel_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        time.sleep(0.1)  # Small delay to ensure GPIO is set

        # Add edge detection on Channel A
        GPIO.add_event_detect(channel_A, GPIO.BOTH, callback=encoder_callback)
        print("Edge detection successfully added to Channel A.")

    except Exception as e:
        print(f"Failed to add edge detection: {e}")
        GPIO.cleanup()  # Reset GPIO to avoid leftover settings
        raise  # Re-raise the exception after cleanup

# Define the callback function for edge detection
def encoder_callback(channel):
    print("Edge detected!")  # Placeholder for actual processing logic

# Run the GPIO setup
try:
    setup_gpio()
    # Main loop to keep script running
    while True:
        time.sleep(0.1)
except Exception as e:
    print(f"Encountered error: {e}")
finally:
    GPIO.cleanup()

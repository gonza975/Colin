import RPi.GPIO as GPIO
import time

channel_a = 17
channel_b = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(channel_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

position = 0
last_state = GPIO.input(channel_a)

try:
    print("Starting manual polling...")
    while True:
        current_state = GPIO.input(channel_a)
        b_state = GPIO.input(channel_b)
        
        if current_state != last_state:  # State has changed
            if b_state != current_state:
                position += 1  # Clockwise
            else:
                position -= 1  # Counter-clockwise
            last_state = current_state
            print(f"Current position: {position}")
        
        time.sleep(0.001)  # Small delay for polling stability

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

def led(color, state):
    if color == 'RED':
        if state:
            GPIO.output(8, GPIO.HIGH) # Turn on led green
            GPIO.output(10, GPIO.LOW) # Turn off led red
        else:
            GPIO.output(8, GPIO.LOW) # Turn off led red

    elif color == 'GREEN':
        if state:
            GPIO.output(8, GPIO.LOW) # Turn on led green
            GPIO.output(10, GPIO.HIGH) # Turn off led red
        else:
            GPIO.output(10, GPIO.LOW) # Turn off led red
    return 'OK'

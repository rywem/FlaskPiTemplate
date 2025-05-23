try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    LED_PIN = 18
    GPIO.setup(LED_PIN, GPIO.OUT)
except (ImportError, RuntimeError):
    # If not on Pi or GPIO lib unavailable
    GPIO = None
    LED_PIN = None

_led_state = False

def toggle_led():
    global _led_state
    _led_state = not _led_state
    if GPIO:
        GPIO.output(LED_PIN, _led_state)

def get_led_status():
    return _led_state


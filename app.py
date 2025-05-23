from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle')
def toggle_led():
    GPIO.output(led_pin, not GPIO.input(led_pin))
    return 'LED toggled!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


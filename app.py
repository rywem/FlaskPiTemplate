from flask import Flask, render_template, redirect, url_for
from gpio_service import toggle_led, get_led_status

app = Flask(__name__)

@app.route('/')
def index():
    status = get_led_status()
    return render_template('index.html', status=status)

@app.route('/toggle')
def toggle():
    toggle_led()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

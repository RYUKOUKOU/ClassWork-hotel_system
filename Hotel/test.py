# app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/room1.html')
def access():
    return render_template('room1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
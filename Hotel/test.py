from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display')
def display():
    return render_template('display.html')

@socketio.on('update_message')
def handle_message(message):
    # 处理从按钮点击事件发送的消息
    socketio.emit('display_message', message)

if __name__ == '__main__':
    socketio.run(app, debug=True)

from flask import Flask,render_template,request,url_for
from flask_socketio import SocketIO
from system import read_info,save_info

main = Flask(__name__)
socketio = SocketIO(main)

@main.route('/')
def index():
    return render_template('index.html')
@main.route('/home.html')
def home():
    return render_template('home.html')
@main.route('/room1.html')
def room1():
    return render_template('room1.html', message="よこそう")
@main.route('/room2.html')
def room2():
    return render_template('room2.html', message="よこそう")

@main.route('/display')
def home1():
    return render_template('display.html')
@socketio.on('update_message')
def handle_message(message):
    # 处理从按钮点击事件发送的消息
    socketio.emit('display_message', message)
    
if __name__ == '__main__':
    main.run(host='0.0.0.0', port=8000)
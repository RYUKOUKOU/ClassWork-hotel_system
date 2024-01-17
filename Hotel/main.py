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

@socketio.on('cleaner')
def handle_button_click(data):
    print(data)
    socketio.emit('update_cleaner', data)
    
if __name__ == '__main__':
    main.run(host='0.0.0.0', port=8000)
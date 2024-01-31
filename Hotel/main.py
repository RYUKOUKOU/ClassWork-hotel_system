from flask import Flask,render_template,request,url_for
from flask_socketio import SocketIO
from system import read_info,save_info
from check_in_out import check_in,check_out

main = Flask(__name__)
socketio = SocketIO(main)

@main.route('/')
def index():
    return render_template('index.html')
@main.route('/home.html')
def home():
    return render_template('home.html')
@main.route('/room101.html')
def room101():
    return render_template('room101.html', message="よこそう")
@main.route('/room102.html')
def room102():
    return render_template('room102.html', message="よこそう")
@main.route('/room103.html')
def room103():
    return render_template('room103.html', message="よこそう")
@main.route('/room201.html')
def room201():
    return render_template('room201.html', message="よこそう")
@main.route('/room202.html')
def room202():
    return render_template('room202.html', message="よこそう")
@main.route('/room203.html')
def room203():
    return render_template('room203.html', message="よこそう")
@main.route('/room301.html')
def room301():
    return render_template('room301.html', message="よこそう")
@main.route('/room302.html')
def room302():
    return render_template('room302.html', message="よこそう")
@main.route('/room303.html')
def room303():
    return render_template('room303.html', message="よこそう")

@main.route('/display')
def home1():
    return render_template('display.html')
@socketio.on('update_message')
def handle_message(id):
    roomid = 'room'+str(id)
    socketio.emit(roomid, '今掃除してもよろしいでしょうか')
@socketio.on('return_message')
def return_message(id):
    socketio.emit('rehome', id)

@socketio.on('roominfo')
def return_message(id):
    a,b,c,d = read_info(id)
    socketio.emit('reroominfo', (a,b,c,d))
@socketio.on('roomin')
def return_message(a,b,c,d):
    check_in(a,b,c,d)
    
if __name__ == '__main__':
    main.run(host='0.0.0.0', port=8000)
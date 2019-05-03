from flask import Flask, jsonify,request,render_template
from flask_socketio import send, emit
from flask_socketio import SocketIO

app = Flask(__name__,template_folder='templates')
socketio =SocketIO(app,namespaces=['/recieve_events'])

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@socketio.on('connect',namespace='/recieve_events')
@app.route('/recieve_events',methods=['GET','POST'])
def recieve_events():
    data=request.get_json()    
    socketio.emit('message',data)    
    return jsonify({'success':"recieved: "+str(data)}),200

@socketio.on('disconnect',namespace='/recieve_events')
def disconnect():
    print('Client disconnected {}'.format(''))
    
if __name__ == '__main__':
    socketio.run(app,port=5000,host='0.0.0.0')
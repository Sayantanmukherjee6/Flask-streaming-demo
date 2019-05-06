from flask import Flask, jsonify,request,render_template
from flask_socketio import send, emit
from flask_socketio import SocketIO
import json

app = Flask(__name__,template_folder='templates')
socketio =SocketIO(app,namespaces=['/recieve_events'])


node_list= [
		{'id': 0, 'label': 'Node 0','shape': 'box'},
		{'id': 1, 'label': 'Node 1','shape': 'box'},
		{'id': 2, 'label': 'Node 2','shape': 'box'},
		{'id': 3, 'label': 'Node 3','shape': 'box'},
		{'id': 4, 'label': 'Node 4','shape': 'box'},
		{'id': 5, 'label': 'Node 5','shape': 'box'},
		{'id': 6, 'label': 'Node 6','shape': 'box'},
		{'id': 7, 'label': 'Node 7','shape': 'box'},
		{'id': 8, 'label': 'Node 8','shape': 'box'},
		{'id': 9, 'label': 'Node 9','shape': 'box'}
	]

def data_process(data):

	for val,node in enumerate(node_list):
		if int(node['id'])==int(data['K']):
			node['color']='#7BE141'
			node_list[val]=node
	return node_list

@app.route('/',methods=['GET','POST'])
def index():
	return render_template("index.html")

@socketio.on('connect',namespace='/recieve_events')
@app.route('/recieve_events',methods=['GET','POST'])
def recieve_events():
	
	global node_list
	data=request.get_json()
	data=data_process(data)	
	socketio.emit('message',json.dumps(data))  
	if all('color' in d for d in data):
		[node.pop('color', None) for node in node_list]
	return jsonify({'success':"recieved: "+str(data)}),200

   
if __name__ == '__main__':
	socketio.run(app,port=5000,host='0.0.0.0')
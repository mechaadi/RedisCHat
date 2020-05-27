from flask import Flask, request, g, render_template
import redis
import json
from flask_socketio import SocketIO, emit, send
import pickle
from flask_cors import CORS, cross_origin
import pickle
import logging
import requests


r = redis.Redis(host='localhost', port=6379, db=0)




# flask app
class App:
    def initApp(self):
        ChatApp = Flask(__name__, template_folder='.')
        CORS(ChatApp)
        ChatApp.config['SECRET_KEY'] = 'secret!'
        socketio = SocketIO(ChatApp, cors_allowed_origins='http://localhost:8085')
        return socketio, ChatApp


App = App()
socketio, app = App.initApp()


def _saveMessage(msg: str, to: str, fr: str, ch: str):
    payload = {
        'msg': msg,
        'to': to,
        'from': fr
    }
    r.rpush('mechaadiList', json.dumps(payload))
    res = r.lrange('mechaadiList', 0, -1)
    return res
    

@cross_origin
@socketio.on('init')
def fetchMessages(ch):
    print('here bitch')
    res = r.lrange(ch, 0, -1)
    res = [json.loads(m) for m in res]
    emit('prevMessages', res, broadcast=True)



  

@cross_origin()
@socketio.on('Message')
def test_message(message):
    print("hehe")
    msgs = _saveMessage(message['msg'], message['to'], message['fr'], message['ch'])
    msgs = [json.loads(msg) for msg in msgs]
    emit('messages', msgs, broadcast=True)

@app.route('/test')
def test():
    r.set()
    return json.dumps({
        'message': 'ok',
        'code': 201
    })

@app.route('/main')
def main():
    return render_template('index.html') 


logging.getLogger('socketio').setLevel(logging.ERROR)

socketio.run(app, host='0.0.0.0', port=8085, debug=True)





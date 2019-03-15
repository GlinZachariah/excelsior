from flask import Flask
from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

def results():
    message=""
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    intent_name = req.get('queryResult').get('intent').get('displayName')
    last_intent= intent_name
    return {'fulfillmentText' : "message"}

@app.route('/paleo',methods=['POST'])
def paleo():
    return make_response(jsonify(results()))

if __name__ == '__main__':
    app.run()

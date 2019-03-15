from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

import disease

app = Flask(__name__)

param ={"parameters": {
          "response": "no",
          "response.original": "bad"
        }}

def final_format_reply(msg,sname,name):
    reponse ={
            "fulfillmentText": ""+msg+"",
            "outputContexts": [
                {
                "name": ""+sname+name+"",
                "lifespanCount": 1,
                "parameters": {
                    "param": "param value"
                }
                }
            ]
            }
    return reponse


@app.route('/')
def hello_world():
    return 'Hello World!'

def results():
    message=""
    req = request.get_json(force=True)
    # action = req.get('queryResult').get('action')
    intent_name = req.get('queryResult').get('intent').get('displayName')
    session_name = req.get('session')
    # last_intent= intent_name
    if intent_name == "iswell":
          print("is well intent")
          name ="/contexts/isfever"
          message = disease.symptoms(req)
          return final_format_reply(message,session_name,name)
    if intent_name == "isfever":
          print("is well intent")
          name ="/contexts/isheadache"
          message = disease.symptoms(req)
          return final_format_reply(message,session_name,name)
    return {'fulfillmentText' : message}

@app.route('/paleo',methods=['POST'])
def paleo():
    return make_response(jsonify(results()))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

import precsription as ps


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

global current

def results():
    message=""
    global current
    req = request.get_json(force=True)
    # action = req.get('queryResult').get('action')
    intent_name = req.get('queryResult').get('intent').get('displayName')

    print("INTENT NAME>>"+intent_name)
    if intent_name == "chickenpox":
          current ="chickenpox"
          message = "You have chickenpox. Would you like to prescribe any medicines?"
    elif intent_name == "nochickenpox":
          current ="typhoid"
          message = "You have Typhoid. Would you like to prescribe any medicines?"
    elif intent_name == "skinrash-yes":
          current ="Measles"
          message = "You have Measles. Would you like to prescribe any medicines?"
    elif intent_name == "shivering-yes":
          current ="Malaria"
          message = "You have Malaria. Would you like to prescribe any medicines?"
    elif intent_name == "swallowbloat-yes":
          current ="Digestive diseases"
          message = "You have Digestive diseases. Would you like to prescribe any medicines?"
    elif intent_name == "badmouth-yes":
          current ="Hyperglycemia"
          message = "You have Hyperglycemia. Would you like to prescribe any medicines?"
    elif intent_name == "irregularbeat-yes":
          current ="High blood pressure"
          message = "You have High blood pressure. Would you like to prescribe any medicines?"
    elif intent_name == "badmouth-yes":
          current ="Hyperglycemia"
          message = "You have Hyperglycemia. Would you like to prescribe any medicines?"
    elif intent_name == "lighthead-yes":
          current ="Migraine"
          message = "You have Migraine. Would you like to prescribe any medicines?"
    if intent_name == "prescribe-yes":
        print("FOUND >>"+current)
        message =ps.prescribe(current)
    return {'fulfillmentText' : message}

@app.route('/paleo',methods=['POST'])
def paleo():
    return make_response(jsonify(results()))

if __name__ == '__main__':
    app.run(debug=True)

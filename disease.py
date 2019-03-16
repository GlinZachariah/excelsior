import json

def symptoms(req):
    intent_name = req.get('queryResult').get('intent').get('displayName')
    parameter_list = req.get('queryResult').get('parameters')
    print(parameter_list['response'])
    if intent_name == "iswell":
        message="Are you having Fever?"
    elif intent_name == "isfever":
        pass
    elif intent_name =="abdominalpain":
        pass
    return message

 
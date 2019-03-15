import json

def symptoms(req):
    parameter_list = req.get('queryResult').get('parameters')
    print(parameter_list['response'])
    message="Are you having Fever?"
    return message

 
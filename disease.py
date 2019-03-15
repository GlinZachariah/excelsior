import json

def symptoms(req):
    parameter_list = req.get('queryResult').get('parameters')
    print(parameter_list['response'])
    message="None"
    return message
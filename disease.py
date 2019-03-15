import json

def claimsby_age(req):
    parameter_list = req.get('queryResult').get('parameters')
    print(parameter_list)
    operation =parameter_list.get('oper')
    message=""
    with open("team-techcrush/data/test_data.json") as datafile:
        data = json.load(datafile)
        dataframe = pd.DataFrame(data)
        t=dataframe
        print(operation)
        if operation == "between":
            min_age =int(parameter_list.get('min_age'))
            max_age =int(parameter_list.get('max_age'))
            s =t[ (t['age']> min_age) & (t['age']< max_age)]['id'].count()
            c =t[ (t['age']> min_age) & (t['age']< max_age)]['claimed_amount'].astype('float64',copy=True,errors='raise')
            message ="There are "+str(s)+" claims for the age "+operation+" of "+str(min_age)+" and "+str(max_age)+" with a total amount of $"+str(int(c.sum()))+"."
        elif operation == "above":
            age =int(parameter_list.get('age')['amount'])
            s =t[ (t['age']> age)]['id'].count() 
            c =t[ (t['age']> age)]['claimed_amount'].astype('float64',copy=True,errors='raise')
            message="The number of claims is "+str(s)+" and the total claimed amount is $"+str(int(c.sum()))+" for the age "+operation+" "+str(age)+"."
    return message
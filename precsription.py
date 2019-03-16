import pandas as pd

def prescribe(disease):
    remedy = []
    medicine = []
    df = pd.read_csv('deseaseremedies.csv', engine='python')
    for row in df.values:
        if row[0].lower() == disease:
            remedy.append(row[1])
            medicine.append(row[2])
    while '-' in medicine:
        medicine.remove('-')
    print (remedy)
    print (medicine[0])
    return medicine[0]


# todo pass automatically
prescribe('migraine')  # input must be lower case
def prescribe(disease):
    import pandas as pd
    remedy =[]
    medicine=[]
    df = pd.read_csv('deseaseremedies.csv', engine='python')
    for row in df.values:
        if row[0].lower()==disease:
            remedy.append(row[1])
            medicine.append(row[2])
    print(remedy)
    print(medicine)


prescribe('chickenpox')

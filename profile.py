from pandas import DataFrame
import pandas as pd


def register(name, age, bgrp, smoke, drink):
    info = {'userinfo': [name, age, bgrp, smoke, drink]}
    df = DataFrame(info)
    df.to_csv(name+'.csv')


def inittimeline(etype, edate, desc, alarm):
    timeline = {'timeline': [etype, edate, desc, alarm]}
    df = DataFrame(timeline)
    print (df)
    df.to_csv('timeline.csv', index=False)


def addtimeline(etype, edate, desc, alarm):
    df = pd.read_csv('timeline.csv', engine='python')
    nextrow = len(df.index)
    df.loc[nextrow] = etype
    nextrow += 1
    df.loc[nextrow] = edate
    nextrow += 1
    df.loc[nextrow] = desc
    nextrow += 1
    df.loc[nextrow] = alarm
    df.to_csv('timeline.csv', index=False)
    print (df)


inittimeline('0', '2018', 'sample', 'none')
addtimeline('1', '2019', 'new', '12:00')
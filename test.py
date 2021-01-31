import datetime
import math
import pandas as pd
from datetime import time
from datetime import date
from matplotlib import pyplot as plt

def printGraph(df,x_axis,y_axis):
    df=df.sort_values(by="Date")
    print(df)
    #y_axis="distance"
    x = df[x_axis]
    y = df[y_axis]
    plt.scatter(x,y)
    plt.show()

def addData(pace):
    # data = {
    #     'Date':['1/19/20','1/14/20','1/17/20','1/16/20'],
    #     'distance':['10','7','8','8'],
    #     'avg_hr':['123','153','152','142'],
    #     'pace':['SS','SS','Intervals','intervals']}
    today=date.today()
    newEntry=([today,'5','152',pace])
    df = pd.read_csv('test.csv')
    print(newEntry)
    df.loc[-1]=newEntry
    df.index = df.index + 1
    df.to_csv(fileName,index=False)
    return df

if __name__ == '__main__':
    addData('00:55:11')
    printGraph(df,'date','distance')
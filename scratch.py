import math
import pandas as pd
from datetime import timedelta
from datetime import date
from matplotlib import pyplot as plt
import numpy as np


def enterData():
    sport=input('Swim, Bike, or Run? ')
    today = date.today()
    #initialize
    totalIntTime = 0

    if sport == 'Swim':
        workoutType = input('What type of workout? Intervals, SteadyState, RP? ')
        if workoutType == 'Intervals':
            numIntervals = int(input('Number of intervals? '))
            for x in range (0,numIntervals):
                timeInput = input('time for interval? (hh:mm:ss) ' )
                totalIntTime = totalIntTime + transformTime(timeInput)
            intDistance = float(input('distance per interval? '))
            totalDistance = intDistance*numIntervals
            avgHR = int(input('Avg HR? '))
            avgIntPace=calcPace(totalIntTime, totalDistance)
            comment = input("Comments: ")
            newEntry = ([today,intDistance,avgIntPace,avgHR,comment])
            df, fileName = addData(sport,workoutType,newEntry)

        elif workoutType == 'SteadyState':
            totalDistance = float(input('distance? '))
            rawTime = input('Total time in hh:mm:ss ? ')
            avgHR = input('Avg HR? ')
            totalSeconds = transformTime(rawTime)
            pace = calcPace(totalSeconds, totalDistance)
            comment = input("Comments: ")
            newEntry = ([today,rawTime,totalDistance,pace,avgHR,comment])
            df, fileName = addData(sport,workoutType,newEntry)

        elif workoutType == 'RP':
            RP_distance = float(input('RP distance? '))
            rawTime = input('Total time in hh:mm:ss ? ')
            RP_avg_hr = input('Avg HR for RP distance? ')
            totalSeconds = transformTime(rawTime)
            RP_avg_pace = calcPace(totalSeconds, RP_distance)
            comment = input("Comments: ")
            newEntry = ([today,RP_distance,RP_avg_pace,RP_avg_hr,comment])
            df, fileName = addData(sport,workoutType,newEntry)
        else:
            enterData()

    elif sport == 'Bike':
        workoutType = input('What type of workout? Intervals, SteadyState, RP? ')
        if workoutType == 'Intervals':
            numIntervals = int(input('Number of intervals? '))
            for x in range (0,numIntervals):
                timeInput = input('time for interval? (hh:mm:ss) ' )
                totalIntTime = totalIntTime + transformTime(timeInput)
            intDistance = float(input('distance per interval? '))
            totalDistance = intDistance*numIntervals
            avgHR = int(input('Avg HR? '))
            int_pwr = int(input('Average Interval Power (W) '))
            avgIntPace=calcPace(totalIntTime, totalDistance)
            comment = input("Comments: ")
            newEntry = ([today,intDistance,avgIntPace,avgHR,int_pwr,comment])
            df, fileName = addData(sport,workoutType,newEntry)

        elif workoutType == 'SteadyState':
            totalDistance = float(input('distance? '))
            rawTime = input('Total time in hh:mm:ss ? ')
            avgHR = input('Avg HR? ')
            totalSeconds = transformTime(rawTime)
            pace = calcPace(totalSeconds, totalDistance)
            comment = input("Comments: ")
            avg_pwr = input("Avg power (W): ")
            newEntry = ([today,rawTime,totalDistance,pace,avgHR,avg_pwr,comment])
            df, fileName = addData(sport,workoutType,newEntry)

        elif workoutType == 'RP':
            RP_distance = float(input('RP distance? '))
            rawTime = input('Total time in hh:mm:ss ? ')
            RP_avg_hr = input('Avg HR for RP distance? ')
            totalSeconds = transformTime(rawTime)
            RP_avg_pace = calcPace(totalSeconds, RP_distance)
            avg_pwr = input("Avg power (W): ")
            comment = input("Comments: ")
            newEntry = ([today,RP_distance,RP_avg_pace,RP_avg_hr,avg_pwr, comment])
            df, fileName = addData(sport,workoutType,newEntry)
        else:
            enterData()

    elif sport == 'Run':
        workoutType = input('What type of workout? Intervals, SteadyState, RP? ')
        if workoutType == 'Intervals':
            numIntervals = int(input('Number of intervals? '))
            for x in range (0,numIntervals):
                timeInput = input('time for interval? (hh:mm:ss) ' )
                totalIntTime = totalIntTime + transformTime(timeInput)
            intDistance = float(input('distance per interval? '))
            totalDistance = intDistance*numIntervals
            avgHR = int(input('Avg HR? '))
            avgIntPace=calcPace(totalIntTime, totalDistance)
            comment = input("Comments: ")
            newEntry = ([today,intDistance,avgIntPace,avgHR,comment])
            df, fileName = addData(sport,workoutType,newEntry)

        elif workoutType == 'SteadyState':
            totalDistance = float(input('distance? '))
            rawTime = input('Total time in hh:mm:ss ? ')
            avgHR = input('Avg HR? ')
            totalSeconds = transformTime(rawTime)
            pace = calcPace(totalSeconds, totalDistance)
            comment = input("Comments: ")
            newEntry = ([today,rawTime,totalDistance,pace,avgHR,comment])
            df, fileName = addData(sport,workoutType,newEntry)

        elif workoutType == 'RP':
            RP_distance = float(input('RP distance? '))
            rawTime = input('Total time in hh:mm:ss ? ')
            RP_avg_hr = input('Avg HR for RP distance? ')
            totalSeconds = transformTime(rawTime)
            RP_avg_pace = calcPace(totalSeconds, RP_distance)
            comment = input("Comments: ")
            newEntry = ([today,RP_distance,RP_avg_pace,RP_avg_hr,comment])
            df, fileName = addData(sport,workoutType,newEntry)
        else:
            enterData()

    else:
        print("Error - ensure correct spelling")
        enterData()

    return fileName

def viewdata():
    sport=input('Swim, Bike, or Run? ')
    category=input("Intervals, RP, SteadyState")
    x_axis = input("What do you want to as x-axis? date? time? distance? avg_hr? ")
    y_axis = input("What do you want to as y-axis? time? distance? avg_hr? pace? avg_pwr? int_pwr? int_distance? avg_int_time? ")
    hyphen = "-"
    fileExt = ".csv"

    fileName=sport+hyphen+category+fileExt
    df = pd.read_csv(fileName)
    df=df.sort_values(by="date")
    x = df[x_axis]
    y = df[y_axis]
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.scatter(x,y)

    plt.show()

def calcPace(totalSeconds,distance):
    pace = round(totalSeconds/(distance*60),2)
    return pace

def transformTime(time):
    splitTime = time.split(":")
    totalSeconds = int(splitTime[0])*3600 + int(splitTime[1])*60 + int(splitTime[2])
    return totalSeconds

def addData(sport,category,newEntry):
    hyphen = "-"
    fileExt = ".csv"
    fileName=sport+hyphen+category+fileExt
    if category == 'SteadyState':
        df = pd.read_csv(fileName)
        if df.empty:
            df.append(newEntry)
            df.to_csv(fileName,index=False)
            return df, fileName

        else:
            df.loc[-1] = newEntry
            df.index = df.index + 1
            return df, fileName

    elif category == 'Intervals':
        if df.empty:
            df.append(newEntry)
            df.to_csv(fileName,index=False)
            return df, fileName
        else:
            df = pd.read_csv(fileName)
            df.loc[-1] = newEntry
            df.index = df.index + 1
            df.to_csv(fileName,index=False)
            return df, fileName

    elif category == 'RP':
        if df.empty:
            df.append(newEntry)
            df.to_csv(fileName,index=False)
            return df, fileName
        else:
            df = pd.read_csv(fileName)
            df.loc[-1] = newEntry
            df.index = df.index + 1
            df.to_csv(fileName,index=False)
            return df, fileName

def compareData(fileName):
    df = pd.read_csv(fileName)
    df = df.sort_values(by='date', ascending=False)
    print('your last workout: ')
    print(df.iloc[0])
    num_for_comparison = int(input('how many of your previous workouts would you like to compare to? '))
    print(df.iloc[0:num_for_comparison])

def seeTotals():
    sport=input('Swim, Bike, or Run? ')
    category=input("Intervals, RP, SteadyState ")
    hyphen = "-"
    fileExt = ".csv"
    fileName=sport+hyphen+category+fileExt
    df = pd.read_csv(fileName)
    df['date'] = pd.to_datetime(df['date'],format="%Y/%m/%d")
    df = df.sort_values(by='date', ascending=False)

    category_to_total = input("what category do you want to see totals for? distance, time ")
    length_of_time = int(input("over how many weeks do you want to see the totals for? "))

    today = date.today()
    min_date = today - timedelta(weeks = length_of_time)
    min_date = np.datetime64(min_date)

    pd_date = df[df.date >= min_date]
    total = pd_date[category_to_total].sum()
    print("total",category_to_total,": ",total)

def clearData():
    sport=input('Swim, Bike, or Run? ')
    category=input("Intervals, RP, SteadyState ")
    hyphen = "-"
    fileExt = ".csv"
    fileName=sport+hyphen+category+fileExt
    df = pd.read_csv(fileName)
    df = df.iloc[0:0]
    return df



#main file
if __name__ == '__main__':
    decision = input("Do you want to enter, view, compare, see totals, or clear data? ")
    if decision == "enter":
        fileName = enterData()
        decision2 = input("do you want to view last 3 similar workouts? yes or no ")
        if decision2 == "yes":
            compareData(fileName)
        else:
             print("Goodbye")
        exit()
    elif decision == "view":
        df = viewdata()
        exit()
    elif decision == "compare":
        sport = input('Swim, Bike, or Run? ')
        category = input('What type of workout? Intervals, RP, or SteadyState? ')
        hyphen = "-"
        fileExt = ".csv"
        fileName = sport+hyphen+category+fileExt
        compareData(fileName)
        exit()
    elif decision == "see totals":
        seeTotals()

    elif decision == "clear data":
        df = clearData()
        print(df)


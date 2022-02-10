# importing the required module
from re import A, S
import matplotlib.pyplot as plt
from ast import Num
import csv
from itertools import count
from lib2to3.pgen2.token import NEWLINE
from operator import neg

with open('2016VizData (2).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    class Weather():
        def __init__(self, categ, station, time):
            self.categ = categ #categories
            self.station = station #stations
            self.time = time #month or year
            self.y_axis = []

        def category(self):
            #if user chooses whole year
            if self.time == 'Y':
                for row in reader:
                    if row['STID'] == self.station:
                    #if self.categ == row[self.categ]:
                        if float(row[self.categ]) < 0:
                            row[self.categ] = 0
                        self.y_axis.append(float(row[self.categ]))

            else:
                #if user chooses specific month
                for row in reader:
                    if row['MONTH'] == self.time and row['STID'] == self.station:
                        if float(row[self.categ]) < 0:
                            row[self.categ] = 0
                        self.y_axis.append(float(row[self.categ]))
                    print(self.y_axis)
    
    u_name = input('Name: ')
    print (f'Welcome {u_name}!')

    
    q = input('What category to look at? (Print TMAX, TMIN, HAVG, WSMX, WSMN, or RAIN): ')
    m = input('Do you want to analyze the entire year or month? (Print Y for year number for month): ')

    r1 = Weather(q, 'ALTU', m)
    r2 = Weather(q, 'BEAV', m)
    r3 = Weather(q, 'NRMN', m)
    r4 = Weather(q, 'TISH', m)
    r5 = Weather(q, 'TULN', m)

    r1.y_axis
    r2.y_axis
    r3.y_axis
    r4.y_axis
    r5.y_axis

    r1.category()

with open('2016VizData (2).csv', newline='') as csvfile: #using this each time because it seems to go away after going through the loop once
    reader = csv.DictReader(csvfile)
    r2.category()

with open('2016VizData (2).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    r3.category()

with open('2016VizData (2).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    r4.category()

with open('2016VizData (2).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    r5.category()

    count = 0
    x_axis = []

    #to number x-axis
    for num in r1.y_axis:
        count += 1
        x_axis.append(count)

    #calling to plot them
    plt.plot(x_axis, r1.y_axis, label = 'ALTU')
    plt.plot(x_axis, r2.y_axis, label = 'BEAV') 
    plt.plot(x_axis, r3.y_axis, label = 'NRMN') 
    plt.plot(x_axis, r4.y_axis, label = 'TISH') 
    plt.plot(x_axis, r5.y_axis, label = 'TULN') 

    # naming the x axis
    plt.xlabel('Days')

    # naming the y axis
    if q == 'TMAX':
        plt.ylabel('Max Temperature')
        plt.title('Max Temperature of Stations')

    if q == 'TMIN':
        plt.ylabel('Min Temperature')
        plt.title('Min Temperature of Stations')

    if q == 'HAVG':
        plt.ylabel('Humilty')
        plt.title('Humilty of Stations')

    if q == 'WSMX':
        plt.ylabel('Max Wind Speed')
        plt.title('Max Wind Speed of Stations')

    if q == 'WSMN':
        plt.ylabel('Min Wind Speed')
        plt.title('Min Wind Speed Stations')

    if q == 'RAIN':
        plt.ylabel('RAIN')
        plt.title('Rain of Stations')
    
    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

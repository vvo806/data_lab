# importing the required module
import matplotlib.pyplot as plt
from ast import Num
import csv
from itertools import count
from lib2to3.pgen2.token import NEWLINE
from operator import neg

'''
# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")
 
# line 2 points
x2 = [1,2,3]
y2 = [4,1,3]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()

'''

# ARD2 points
with open('BigData2016 (1).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    x = [*range (1,367,1)]
    ARD2_y = []
    BEAV_y = []
    BOIS_y = []
    CENT_y = []
    NRMN_y = []
    STIL_y = []
    TISH_y = []
    TULN_y = []
    WOOD_y = []

    for row in reader:
        if row['STID'] == 'ARD2':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            ARD2_y.append(float(row['TMAX']))

        if row['STID'] == 'BEAV':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            BEAV_y.append(float(row['TMAX']))

        if row['STID'] == 'BOIS':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            BOIS_y.append(float(row['TMAX']))

        if row['STID'] == 'CENT':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            CENT_y.append(float(row['TMAX']))

        if row['STID'] == 'NRMN':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            NRMN_y.append(float(row['TMAX']))

        if row['STID'] == 'STIL':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            STIL_y.append(float(row['TMAX']))

        if row['STID'] == 'TISH':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            TISH_y.append(float(row['TMAX']))

        if row['STID'] == 'TULN':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            TULN_y.append(float(row['TMAX']))

        if row['STID'] == 'WOOD':
            if float(row['TMAX']) < 0:
                row['TMAX'] = 0

            WOOD_y.append(float(row['TMAX']))

    plt.plot(x, ARD2_y, label = 'ARD2')
    plt.plot(x, BEAV_y, label = 'BEAV')
    plt.plot(x, BOIS_y, label = 'BOIS')
    plt.plot(x, CENT_y, label = 'CENT')
    plt.plot(x, NRMN_y, label = 'NRMN')
    plt.plot(x, STIL_y, label = 'STIL')
    plt.plot(x, TISH_y, label = 'TISH')
    plt.plot(x, TULN_y, label = 'TULN')
    plt.plot(x, WOOD_y, label = 'WOOD')

    # naming the x axis
    plt.xlabel('Days')
    # naming the y axis
    plt.ylabel('Temperature')
    # giving a title to my graph
    plt.title('Temperature of 9 Stations')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()



'''
    for row in reader:
        station = 'ARD2'
        num = float(row('TMAX'[station]))
        if num < 0:
            num = 'None'

        ARD2_y.append(float(row('TMAX'['ARD2'])))


    plt.plot(ARD2_x, ARD2_y, label = "ARD2")

    # naming the x axis
    plt.xlabel('Day')
    # naming the y axis
    plt.ylabel('Temperature')
    # giving a title to my graph
    plt.title('Temperature of 9 Stations')

    # show a legend on the plot
    plt.legend()
 
    # function to show the plot
    plt.show()
'''

'''
    num = ARD2_x[0]

    for n in ARD2_x:
        if n > num:
            num = n

    print(f"Highest max = {num}")


with open('BigData2016 (1).csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(f"TMAX = {row['TMAX']}, TMIN = {row['TMIN']}")
'''
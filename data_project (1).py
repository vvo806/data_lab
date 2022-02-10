# importing the required module
from re import A, S
import matplotlib.pyplot as plt
from ast import Num
import csv
from itertools import count
from lib2to3.pgen2.token import NEWLINE
from operator import neg

'''
with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

class Weather(object):
    def __init__(self, month, day, station, temp_max, temp_min, hum, ws_max, ws_min, rain):
        self.month = month
        self.day = day
        self.station = station
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.hum = hum
        self.ws_max = ws_max
        self.ws_min = ws_min
        self.rain = rain
    
    def sta(self):
        with open('2016VizData.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
        
        x = []
        for row in reader:
            if row['STID'] == {station}:
                pass

category = ['Temp_Max', 'Temp_Min', 'Humidlty', 'WS_Max', 'WS_Min']
class ALTU():
    with open('2016VizData (2).csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

    def __str__(self):
        return f'{self.station}'

    def cat(self):
        count = 1
        for subject in category:
            print(f'{count}: {subject}')
            count += 1

        subject = int(input('What category do you want to see?: '))

        if subject == 1:
            subject = ALTU('ALTU')
            print(subject.temp_max)

    def __init__(self, station):
        #self.month = month
        #self.day = day
        self.station = station
        #self.temp_max = temp_max
        #self.temp_min = temp_min
        #self.hum = hum
        #self.ws_max = ws_max
        #self.ws_min = ws_min
        #self.rain = rain

    def temp_max(self):
        y = []
        for row in reader:
            if row['STID'] == 'ALTU':
                if float(row['TMAX']) < 0:
                    row['TMAX'] = 0

            y.append(float(row['TMAX']))

        print(y)

month = [*range (1,13,1)]
day = [*range (1,32,1)]

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    ALTU = Weather(month, day, 'ARD2', 'TMAX', 'TMIN', 'HAVG', 'WSMX', 'WSMN', 'RAIN')

    for row in reader:
        print(float(row[ALTU.temp_max]))

    #for row in reader:
       #print(float(row[ARD2.temp_max]))

    x = [*range (1,367,1)] #x-axis
    ARD2_y = [] #y-axis
    BEAV_y = []
    BOIS_y = []
    CENT_y = []
    NRMN_y = []
    STIL_y = []
    TISH_y = []
    TULN_y = []
    WOOD_y = []

    y = []

    count = 0
    for row in reader:
        y.append(float(row['TMAX']))
        count += 1

    print(y)
    print(count)

    #pl = Weather(1, 2, "ALTU", float(row["TMAX"]), "TMIN", "HAVG", "WSMX", "WSMN", "RAIN")

    #print(pl.temp_max)


station_list = [ALTU('ALTU'), 'BEAV', 'NRMN', 'TISH', 'TULN']
#category = ['Temp_Max', 'Temp_Min', 'Humidlty', 'WS_Max', 'WS_Min']
u_name = input('Name: ')
print(f'Welcome {u_name}!')

num = 1
for stations in station_list:
    print(f'{num}: {stations}')
    num += 1

station = int(input('Which station do you want to see?: '))

while stations == 1:
    stations = ALTU()
    stations.cat()

count = 1
for subject in category:
    print(f'{count}: {subject}')
    count += 1

subject = int(input('What category do you want to see?: '))

if subject == 1:
    subject = ALTU('ALTU')
    print(subject.temp_max)
'''

with open('2016VizData (2).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    class Weather():
        def __init__(self, categ, station):
            self.categ = categ
            self.station = station

        def category(self):
            for row in reader:
                if row['STID'] == self.station:
                    if float(row[self.categ]) < 0:
                        row[self.categ] = 0
                    y_axis.append(float(row[self.categ]))
                print(y_axis)
    
    u_name = input('Name: ')
    print (f'Welcome {u_name}!')

    y_axis = []
    q = input('What category to look at? (Print TMAX, TMIN, HAVG, WSMX, WSMN, or RAIN): ')
    s = input('What station? (Print ALTU, BEAV, NRMN, TISH, or TULN): ')
    r1 = Weather(q,s)
    r1.category()

    x_axis = [*range (1,367,1)]

    #calling to plot them
    plt.plot(x_axis, y_axis, label = 'ALTU') 

    # naming the x axis
    plt.xlabel('Days')
    # naming the y axis
    if q == 'TMAX':
        plt.ylabel('Max Temperature')
        plt.title('Max Temperature of Station')

    if q == 'TMIN':
        plt.ylabel('Min Temperature')
        plt.title('Min Temperature of Station')

    if q == 'HAVG':
        plt.ylabel('Humilty')
        plt.title('Humilty of Station')

    if q == 'WSMX':
        plt.ylabel('Max Wind Speed')
        plt.title('Max Wind Speed of Station')

    if q == 'WSMN':
        plt.ylabel('Min Wind Speed')
        plt.title('Min Wind Speed Station')

    if q == 'RAIN':
        plt.ylabel('RAIN')
        plt.title('Rain of Station')
    
    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

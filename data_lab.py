from ast import Num
import csv
from itertools import count
from lib2to3.pgen2.token import NEWLINE
from operator import neg

'''
with open('names.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['first_name'], row['last_name'])
'''

with open('Norman2016.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(f"TMAX = {row['TMAX']}, TMIN = {row['TMIN']}") #'TMAX' and 'TMIN' row will be the only thing print out

# Average TMAX data
with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    data = []

    for row in reader:
        if float(row['TMAX']) > 0:
            data.append(float(row['TMAX']))

    avg = sum(data) / len(data)
    print(f"Avg TMAX = {avg}")


# Average TMIN data
with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    data = []

    for row in reader:
        if float(row['TMIN']) > 0:
            data.append(float(row['TMIN']))

    avg = sum(data) / len(data)
    print(f"Avg TMIN = {avg}")


# Finding highest max temp.
with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    max = []

    for row in reader:
        max.append(float(row['TMAX']))

    num = max[0]

    for n in max:
        if n > num:
            num = n

    print(f"Highest max = {num}")


# Finding highest min temp.
with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    min = []

    for row in reader:
        min.append(float(row['TMIN']))

    numb = min[0]

    for m in min:
        if m > numb:
            numb = m

    print(f"Highest min = {numb}")
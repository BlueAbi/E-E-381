import csv, matplotlib.pyplot as plt

years = (2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020)

def truncate(num, n):                 ## truncate to n decimal places
    return int(num * 10 ** n) / 10 ** n

def calc_mean(reader, year) :
    total = 0
    year_num = 0

    for row in reader:
        if int(row[0]) == year :
            total += int(row[1])
            year_num += 1

    if year_num > 0 :
        return total / year_num
    else :
        return 0

with open("Sales_01_20.csv", newline="") as f :
    reader = csv.reader(f)
    next(reader)    ## skip the first line in the csv
    average = truncate(calc_mean(reader), 2)
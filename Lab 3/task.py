#!/usr/bin/env python

import csv
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def getCityLocation(csvData,cityIndex,latIndex,lonIndex):
    cityName = raw_input("Enter city name: ")
    coordinates = []
    for rows in csvData:
        if(rows[cityIndex] == cityName):

            coordinates.append(rows[lonIndex])
            coordinates.append(rows[latIndex])
            return coordinates






cityDataFile = open('GeoLiteCity-Location.csv')

cityDataReader= csv.reader(cityDataFile)
cityData = list(cityDataReader)

del cityData[:1]
# it = 0
# for rows in cityData:
#     if(it==10):
#         break
#     print (rows)
#     it+=1

latCol = cityData[0].index('latitude')
lonCol = cityData[0].index('longitude')
cityCol = cityData[0].index('city')



print "1. Find a city's coordinates\n2. Find nearby city\n3.Exit"

option = raw_input("Enter Option: ")

while not int(option) == 3:
    if int(option) == 1:
        cityLocation = getCityLocation(cityData,cityCol,latCol,lonCol)
        print "longitude: ", cityLocation[0]
        print "latitude: ", cityLocation[1]
        print "\n"

    if int(option) == 2:
        numCity = raw_input("Enter number of nearby to be found: ")
        suboption = raw_input ("a. City Name\nb. Latitude/Longitude: ")

        if suboption == 'a':
            print "Entered"
            cityLocation = getCityLocation(cityData,cityCol,latCol,lonCol)
            cityLongitude = cityLocation[0]
            cityLatitude = cityLocation[1]

            print cityLongitude
            print cityLatitude
            cityNames = []
            it = 0
            for rows in cityData[1:]:

                if it == int(numCity):
                    break

                if haversine(float(cityLongitude), float(cityLatitude), float(rows[lonCol]), float(rows[latCol])) <1000:
                    cityNames.append(rows[cityCol])
                    it+=1

            print cityNames
        if suboption == 'b':
            latitude = raw_input("Enter latitude: ")
            longitude = raw_input("Enter longitude: ")
            cityNames = []

            it = 0

            for rows in cityData[1:]:
                if it == int(numCity):
                    break
                if haversine(float(longitude), float(latitude), float(rows[lonCol]), float(rows[latCol])) <1000:
                    cityNames.append(rows[cityCol])
                    it+=1

            print cityNames


    print "1. Find a city's coordinates\n2. Find nearby city\n3.Exit"
    option = raw_input("Enter Option: ")

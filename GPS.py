import time
import random
import requests


def moveeast(lat, long):
    long += .0009
    return long

def movenorth(lat, long):
    lat += .0009
    return lat

def movewest(lat, long):
    long -= .0009
    return long

def movesouth(lat, long):
    lat -= .0009
    return lat

def move():
    lat = 36.04866710899252
    long = -94.18507413935218
    location = {
        "lat": lat,
        "long": long
    }
    while(True):
        while(long < -94.18062079836531):
            long = moveeast(lat, long)
            ## WRITE LONG TO DB HERE
            location["long"] = long
            print(requests.post("https://geobus-app-api.herokuapp.com/vehicles/update/position/1", json = location))
            time.sleep(500)
        while(lat < 36.05666733331742):
            lat = movenorth(lat, long)
            ## WRITE LAT TO DB HERE
            location["lat"] = lat
            print(requests.post("https://geobus-app-api.herokuapp.com/vehicles/update/position/1", json = location))
            time.sleep(500)
        while(long > -94.18504237244547):
            long = movewest(lat, long)
            ## WRITE LONG TO DB HERE
            location["long"] = long
            print(requests.post("https://geobus-app-api.herokuapp.com/vehicles/update/position/1", json = location))
            time.sleep(500)
        while(lat > 36.04875525081654):
            lat = movesouth(lat, long)
            location["lat"] = lat
            print(requests.post("https://geobus-app-api.herokuapp.com/vehicles/update/position/1", json = location))
            time.sleep(500)

def main():
    move()

if __name__ == '__main__':
    main()

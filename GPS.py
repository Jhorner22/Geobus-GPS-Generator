import time
import random


def moveeast(long):
    long += .00001
    return long

def movenorth(lat):
    lat += .0001
    return lat

def movewest(long):
    long -= .0001
    return long

def movesouth(lat):
    lat -= .0001
    return lat

def move():
    lat = 36.04866710899252
    long = -94.18507413935218
    while(True):
        while(long < -94.18062079836531):
            long = moveeast(long)
            ## WRITE LONG TO DB HERE
            time.sleep(500)
        while(lat < 36.05666733331742):
            lat = movenorth(lat)
            ## WRITE LAT TO DB HERE
            time.sleep(500)
        while(long > -94.18504237244547):
            long = movewest(long)
            ## WRITE LONG TO DB HERE
            time.sleep(500)
        while(lat > 36.04875525081654):
            lat = movesouth(lat)

def main():
    move()

if __name__ == '__main__':
    main()

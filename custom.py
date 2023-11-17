import datetime

def getYear():
    currentDate = datetime.datetime.now()
    currentYear = currentDate.year
    print(currentYear)

getYear()

def myMap():
    mapProp = {
        "center": (40.712775, -74.005973),
        "zoom": 18
    }

    print("Map created")

myMap()


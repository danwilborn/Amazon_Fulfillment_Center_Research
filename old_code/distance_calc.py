import sys, json, re, math
from urllib2 import Request, urlopen, URLError

def readin_coordinates():
    
    latitude = 33.433156 
    longitude = -112.207478
    origins = (latitude, longitude)
    point_calculator(origins)
    #print(origins)

def point_calculator(origins):

    latitude, longitude = origins
    destinations = list()
    rad = math.radians(30)
    miles = 30
    distance = float(miles/69)
    for i in range(0, 12):
        new_latitude = latitude + distance*math.sin(30*i)
        new_longitude = longitude + distance*math.cos(30*i)
        destinations.append((new_latitude, new_longitude))      

    distance_call(origins, destinations)

def distance_call(origins, destinations):

    origin_latitude, origin_longitude = origins
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=YOUR_API_KEY'            
    r = Request(url)
    try:
        response = urlopen(r)
        data = response.read()
    except URLError as e:
        print("URL request error: ", e)

    data = json.loads(data)
    print(data)

def main():
    readin_coordinates()    

main()

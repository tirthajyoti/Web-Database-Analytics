
"""
This code uses Google Map's Geolocation API to retreive latitude and longitude for any location on Earth that user types in
"""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location (enter \'quit\' to quit): ')
    if len(address) < 1 or address=='quit': break

    # Appends the input location (address to search for) to the URL string
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)

    # Request the URL
    uh = urllib.request.urlopen(url)
    # Read the decoded URL data
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    # Builds the XML element tree
    tree = ET.fromstring(data)
    # Check if the returned status is OK. If not then breaks the loop and exits.
    status = tree.find('status').text
    if status!='OK':
        print('Could not retrive')
        break
    # Looks for the 'result' element in the data and extracts latitude and longitude from it
    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text
    
    # Prints the final results
    print('Latitude:', lat)
    print('Longitude:', lng)
    print('Formatted address:',location)





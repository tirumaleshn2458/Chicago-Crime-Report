import argparse
parser = argparse.ArgumentParser(description="None", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--file_number',type=str,help='file_number')
args = vars(parser.parse_args())
file_number=args['file_number']
import requests
new_coordinates={}
def get_coordinates(address):
    url = f"https://geocode.xyz/{address}?json=1"

    try:
        # Make a GET request to the Geocode.xyz API
        response = requests.get(url)
        data = response.json()

        # Check if coordinates are found
        if 'latt' in data and 'longt' in data:
            latitude = data['latt']
            longitude = data['longt']
            #print(f"Coordinates for {address}: Latitude = {latitude}, Longitude = {longitude}")
            #coordinates_new.append((latitude,longitude))
            return (latitude,longitude)
        else:
            print(f"No coordinates found for {address}")
            return 0
    except Exception as e:
        print("Error:", e)

# Example usage:
#address = "W 73RD ST, Chicago, Illinois"
#get_coordinates(address)

import time
import json
start_time=time.time()
with open(f'no_coordinates{file_number}.json','r') as file:
    no_list=json.load(file)
for address in no_list['no_list']:
    try_number=0
    print(address)
    while True:
        print('Try Number: ',try_number)
        coordinates=get_coordinates(address)
        if coordinates==0:
            print('---------------------------------------------------------------------')
            print('No address for this')
            print('---------------------------------------------------------------------')
            print('---------------------------------------------------------------------')
            break
        try:
            float(coordinates[0])
            print(coordinates)
            new_coordinates[address]=coordinates
            break
        except:
            try_number=try_number+1
            pass
    print('-----------------------------')
end_time=time.time()
print('Total time taken: ',end_time-start_time)
with open(f'new_coordinates{file_number}.json','w') as file:
    json.dump(new_coordinates,file)

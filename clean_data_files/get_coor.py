import argparse
parser = argparse.ArgumentParser(description="None", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--start_index", type=int, help="start_index")
parser.add_argument('--end_index',type=int,help='end_index')
parser.add_argument('--file_number',type=str,help='file_number')
args = vars(parser.parse_args())
start_index=args['start_index']
end_index=args['end_index']
file_number=args['file_number']

import json
import requests

coordinates={}
no_address=[]
with open('uni_address.json','r') as file:
    uni_address_dict=json.load(file)
uni_address=uni_address_dict['uni_address']
def get_coordinates(place_name):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place_name,
        "format": "json",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        return float(data[0]['lat']), float(data[0]['lon'])
    else:
        return None, None


index_values=range(len(uni_address[start_index:end_index]))
for place_name,i in zip(uni_address[start_index:end_index],index_values):
    if i%50==0:
        print(i)
    latitude, longitude = get_coordinates(place_name)
    if latitude is not None and longitude is not None:
        coordinates[place_name]=(latitude,longitude)
        #print(f"Coordinates for {place_name}: Latitude={latitude}, Longitude={longitude}")
    else:
        print(f"Coordinates for {place_name} not found.")
        no_address.append(place_name)

#saving the first dictionary of around 1000 coordinates
with open(f'coordinates{file_number}.json','w') as file:
    json.dump(coordinates,file)

no_coordinates={'no_list':no_address}
with open(f'no_coordinates{file_number}.json','w') as file:
    json.dump(no_coordinates,file)

with open(f'no_coordinates{file_number}.json','r') as file:
    no_list=json.load(file)

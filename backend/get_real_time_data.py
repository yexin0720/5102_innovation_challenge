import requests
import pandas as pd
from fuzzywuzzy import process
import requests

def get_data(api_key='YfWoD5wkQ2SvYbRnNyxLQw=='):
    # url = "http://datamall2.mytransport.sg/ltaodataservice/EstTravelTimes"
    # url = "http://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2"
    # url = "http://datamall2.mytransport.sg/ltaodataservice/TrafficFlow"
    url = "http://datamall2.mytransport.sg/ltaodataservice/Traffic-Imagesv2"
    headers = {
        "AccountKey": api_key,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print("Already get the real time Traffic Images data!")
        return data
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None
    
# Use google map API to get the real location coordinates based on address
def get_location_coordinate(address):
    api_key = "AIzaSyA4XlLwJ8VsbrmA-F67RoN91VRDk8K0ZS0"
    # api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&components=country:SG&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        return latitude, longitude


def get_distance(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Use google map API to get the real location name based on lat&lng
def get_location_name(lat, lng, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{lat},{lng}",
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            # Get the formatted address of the first result
            location_name = data["results"][0]["formatted_address"]
            return location_name
    return None

def location_split(list):
    camera_location_split = []
    for i in list: 
        # print(i.split(',', 1)[0])
        camera_location_split.append(i.split(',', 1)[0])
    return camera_location_split

def get_best_match(camera_data, latitude, longitude):
    best_match = None
    camera_data = pd.DataFrame(camera_data['value'])
    for i in range(len(camera_data)):
        lat, lng = camera_data['Latitude'][i], camera_data['Longitude'][i]
        distance = get_distance(lat, latitude, lng, longitude)
        if not best_match or distance < best_match[1]:
            best_match = (i, distance)
    return camera_data.iloc[best_match[0]]["ImageLink"]

def get_real_time_data_final_process():
    LTA_api_key = "YfWoD5wkQ2SvYbRnNyxLQw=="
    camera_data = get_data(LTA_api_key)
    camera_data = pd.DataFrame(camera_data['value'])
    # if camera_data:
    #     for i in camera_data['value']:
    #         print(i['Latitude'], i['Longitude'])
    goole_map_api_key = "AIzaSyA4XlLwJ8VsbrmA-F67RoN91VRDk8K0ZS0"
    if not camera_data.empty:
        camera_location_list = []
        for i in range(len(camera_data)):
            lat, lng = camera_data['Latitude'][i], camera_data['Longitude'][i]
            # print(lat, lng)
            location_name = get_location_name(lat, lng, goole_map_api_key)
            if location_name:
                # print(location_name)
                camera_location_list.append(location_name)
            else:
                print("Failed to retrieve location name.")
    camera_location_split = location_split(camera_location_list)
    return camera_data, camera_location_list, camera_location_split


if __name__ == '__main__':
    camera_data = get_data()
    camera_data = pd.DataFrame(camera_data['value'])
    best_match = get_best_match(camera_data, 1.29939, 103.7799)
    print(best_match['ImageLink'])


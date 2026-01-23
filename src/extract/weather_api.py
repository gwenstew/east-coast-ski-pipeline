import requests
import json
import os
from src.utils.config import API_KEY



def fetch_weather_data(location, date1, date2):
    """
    Extract weather data from visual crossing from range of dates
    saves JSON response in raw_json
    
    :param location: mountain
    :param date1: start date yyyy-MM-dd
    :param date2: end date yyyy-MM-dd
    """
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date1}/{date2}?key={API_KEY}&include=days"

    response = requests.get(url)
    weather = response.json()

    # save json to file in /data for later use 
    filepath = f"data/raw/weather/{location}-{date1}-{date2}.json"
    with open(filepath, 'w') as json_file:
        json.dump(weather, json_file, indent=4)

    return weather

def main():
    location = "Havertown,PA"
    date1 = "2026-01-14"
    date2 = "2026-01-15"

    fetch_weather_data(location, date1, date2)

    # TODO: load results into postgres
    

if __name__=="__main__":
    main()

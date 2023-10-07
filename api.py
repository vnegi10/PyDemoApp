# Fetch temperature forecast data from Open-Meteo API

import requests
import json
import pandas as pd
from tabulate import tabulate

def get_temp_url(lat, long):
    url1 = 'https://api.open-meteo.com/v1/forecast?'
    url2 = 'latitude={lat}&longitude={long}&hourly=temperature_2m'.format(lat = str(lat), long = str(long))
    return url1 + url2

def make_request(lat, long):
    url = get_temp_url(lat, long)
    response = requests.get(url)
    if (response.status_code) == 200:
        print("Success!")
    else:
        print("Something went wrong!")
    return response

def get_temp_data(lat, long):
    response = make_request(lat, long)
    temp_data = response.json()['hourly']['temperature_2m']
    time = response.json()['hourly']['time']
    return pd.DataFrame({'time': time,
                         'temperature': temp_data})

def jprint(obj):
    # Create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Test with Veldhoven coordinates
df_temp = get_temp_data(51.4176, 5.4060)
print(tabulate(df_temp, headers = 'keys', tablefmt = 'psql'))


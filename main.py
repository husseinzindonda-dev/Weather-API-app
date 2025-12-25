#==== Block 1: Importing Statements ====
# What modules does the program need to import to function correctly?
import os
import json
import requests
from dotenv import load_dotenv

#==== Block 2: Loading Configurations ====
# How will the program securely access the API key?
load_dotenv() # This reads the .env file
API_KEY = os.getenv('OPENWEATHER_API_KEY')  # Accesses the API key from the .env file
# CRITICAL CHECK: Is API_KEY 'None' or does it contain a valid key?
# How would you print it to verify (an then remove the print statement)?
print(API_KEY)  # Uncomment this line to check if the API_KEY is loaded correctly
#==== Block 2.5: Unit Choice Function ====
def get_unit_preference():
    """Ask user for temperature unit preference."""
    while True:
        unit = input("Choose temperature unit - Celsius (C) or Fahrenheit (F): ").strip().upper()
        if unit == 'C':
            return 'metric' 
        elif unit == 'F':
            return 'imperial'
        else:
            print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

#==== Block 3: Function Definition ====
# Define function for each major task
def get_coordinates(city_name, api_key):
    """Step 2 & 3: Call GeoCoding API and get lat/lon coordinates"""
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city_name,
        "limit": 1,
        "appid": api_key
    }
    try:
        response = requests.get(geo_url, params=params, timeout=10)
        response.raise_for_status()  # Raises an exception for 4XX/5XX errors
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None, None
    
def get_weather(lat, lon, api_key, units='metric'):
    """Step 4 & 5: Call Current Weather API and parse data"""
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": units
    }
    response = requests.get(weather_url, params=params)
    data = response.json()
    #("\n=== FULL API RESPONSE ===")
   # print(json.dumps(data, indent=2))
    if 'main' in data and 'weather' in data:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data.get('main', {}).get('humidity', 'N/A')
        wind_speed = data.get('wind', {}).get('speed', 'N/A')
        return {
            "temp": temperature,
            "description": description,
            "humidity": humidity,
            "wind_speed": wind_speed
        }
    else:
        return None, None, None, None
    
#==== Block 4: Main Program Execution ====
# Main program logic
if __name__ == "__main__":
    units = get_unit_preference()
    city_name = input("Enter the name of the city: ")
    lat, lon = get_coordinates(city_name, API_KEY)
    if lat is None or lon is None:
        print(f"Error: Could not find coordinates for '{city_name}'.Please check the city name and try again.")
    else:
        weather_data = get_weather(lat, lon, API_KEY, units)
        temperature, description, humidity, wind_speed = weather_data
        print(f"Current temperature in {city_name}: {weather_data['temp']}° {'C' if units == 'metric' else 'F'}")
        print(f"Conditions: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
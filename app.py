from flask import Flask, render_template, request
import os
import requests
from dotenv import load_dotenv

# load environment variables
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

app = Flask(__name__)

# add your existing functions (or import them)
def get_coordinates(city_name, api_key):
    """Step 2 & 3: Call GeoCoding API and get lat/lon coordinates"""
    import requests
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
    import requests
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": units
    }
    try:
        response = requests.get(weather_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    # Get city from form
    city = request.form.get('city', '').strip()

    if not city:
        return "Please enter a city name.", 400
    
    # Get coordinates
    lat, lon = get_coordinates(city, API_KEY)
    if lat is None or lon is None:
        return f"Could not find city: {city}.", 404

    # Call functions from main.py to get weather data
    weather_data = get_weather(lat, lon, API_KEY, units='metric')

    # Pass to template
    return render_template('weather.html',
                           city=city,
                           temp=weather_data['temp'],
                           description=weather_data['description'],
                            humidity=weather_data['humidity'],
                            wind_speed=weather_data['wind_speed'])



if __name__ == '__main__':
    app.run(debug=True)
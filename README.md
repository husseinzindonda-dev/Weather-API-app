# 🌤️ Weather Dashboard

A clean, responsive web application built with Flask that displays current weather conditions for any city using the OpenWeather API.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## ✨ Features

- **Real-time Weather Data**: Current temperature, humidity, wind speed, and conditions
- **City Search**: Enter any city worldwide to get instant weather information
- **Clean UI**: Responsive design with intuitive user interface
- **Error Handling**: Graceful error messages for invalid cities or API issues
- **Metric/Imperial Units**: Supports both Celsius and Fahrenheit (planned enhancement)


## 📁 Project Structure

weather-dashboard/

├── app.py                 # Main Flask application

├── requirements.txt       # Python dependencies

├── .env                  # Environment variables (API key)

├── .gitignore            # Git ignore file

├── README.md             # This file

├── static/               # Static assets

    └── style.css         # Stylesheet

└── templates/            # HTML templates

    ├── index.html        # Homepage with search form

    └── weather.html      # Weather results page



## 🔧 How It Works
1. User Input
User enters a city name in the search form

Form submits to Flask backend via POST request

2. Backend Processing
python
# Simplified flow:
city → get_coordinates() → (lat, lon) → get_weather() → weather data → template

3. API Integration
Geocoding API: Converts city name to latitude/longitude

Current Weather API: Fetches weather data using coordinates

Error Handling: Validates responses and handles API errors gracefully

4. Frontend Display
Jinja2 templates render dynamic data

CSS provides responsive styling

Clean, user-friendly interface

# 🛠️ Technologies Used
Backend: Python, Flask, Requests

Frontend: HTML5, CSS3, Jinja2 templating

API: OpenWeatherMap REST API

Environment: python-dotenv for configuration management

# 🔌 API Reference
This project uses two OpenWeather API endpoints:

Geocoding API: api.openweathermap.org/geo/1.0/direct

Converts city names to geographic coordinates

Required parameters: q (city name), appid (API key)

Current Weather API: api.openweathermap.org/data/2.5/weather

Fetches current weather data

Required parameters: lat, lon, appid, units (metric/imperial)

# 🧪 Testing
Test the application with various scenarios:

# Edge cases
"", "InvalidCityName123", cities with special characters

# 🚧 Future Enhancements
Planned features and improvements:

5-day weather forecast

Temperature unit toggle (Celsius/Fahrenheit)

Location detection via browser geolocation

Weather icons matching conditions

Air quality index display

Historical weather data

Multi-language support


📄 License
This project is licensed under the MIT License.


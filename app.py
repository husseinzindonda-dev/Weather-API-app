from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    # Get city from form
    city = request.form.get('city', '')

    #TODO: Call functions from main.py to get weather data

    #TODO: Render weather data in template
    return render_template('weather.html', city=city)

if __name__ == '__main__':
    app.run(debug=True)
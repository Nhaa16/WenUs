from flask import Flask
from flask import render_template, url_for, request, redirect
app = Flask(__name__)
import pyowm
from datetime import datetime
from gpiozero import LED
from time import sleep

@app.route('/')
def index():
    return render_template('home.html')


@app.route("/weather")
def weather():
    return render_template('weather.html')


@app.route("/weather/submit", methods=['GET', 'POST'])
def submit():
    user_input_1=request.form.get('city')
    user_input_2=request.form.get('country')
        
    place = user_input_1 + ", " + user_input_2
    print(place)

    apikey = '51c6723dd2f51626dd33896729e79676'
    owm = pyowm.OWM(apikey)
    observation = owm.weather_at_place(place)
    w = observation.get_weather()

    winds = w.get_wind()
    humidities = w.get_humidity()
    tempreture = w.get_temperature()
    presh = w.get_pressure()
    clud = w.get_clouds() 
    ran = w.get_rain() 
    snow = w.get_snow()                          
    sunr = w.get_sunrise_time('iso')
    suns = w.get_sunset_time('iso')
    style = w.get_detailed_status()
    ref = w.get_reference_time(timeformat='iso')
    
    tem = {"City": user_input_1, "Country": user_input_2, "Wind" : winds, "Humidity" : humidities, "Temperature" : tempreture,
           "Pressure" : presh, "Cloud" : clud, "Rain" : ran, "Snow" : snow, "Sunrise Time" : sunr, "Sunset Time" : suns,
            "Weather View" : style, "Referenced Time" : ref}
    
     
    return render_template('submit.html', index = tem)
 
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

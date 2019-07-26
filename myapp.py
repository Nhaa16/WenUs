
from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)
import pyowm
from gpiozero import LED
from time import sleep

@app.route('/')
def index():

    location = 'London, UK'
    apikey = '51c6723dd2f51626dd33896729e79676'
    owm = pyowm.OWM(apikey)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()

    

#    winds = w.get_wind()
#    humidities = w.get_humidity()
    tempreture = w.get_temperature()
#    presh = w.get_pressure()
#    clud = w.get_clouds()
#    ran = w.get_rain()
#    snow = w.get_snow()
    tem = tempreture
    


    return render_template('home.html', index = tem)



@app.route("/weather")
def weather():
    return render_template('weather.html')


@app.route("/weather/submit")
def submit():
    
    location = 'London, UK'
    apikey = '51c6723dd2f51626dd33896729e79676'
    owm = pyowm.OWM(apikey)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()

    

#    winds = w.get_wind()
#    humidities = w.get_humidity()
    tempreture = w.get_temperature()
#    presh = w.get_pressure()
#    clud = w.get_clouds()
#    ran = w.get_rain()
#    snow = w.get_snow()
    tem = tempreture
    return render_template('submit.html', index = tem)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

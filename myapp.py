from flask import Flask
from flask import render_template, url_for, request
app = Flask(__name__)
import pyowm
from gpiozero import LED
from time import sleep

@app.route('/')
def index():

#    location = 'London, UK'
#    apikey = '51c6723dd2f51626dd33896729e79676'
#    owm = pyowm.OWM(apikey)
#    observation = owm.weather_at_place(location)
#    w = observation.get_weather()
#
#
#
#    winds = w.get_wind()
#    humidities = w.get_humidity()
#    tempreture = w.get_temperature()
#    presh = w.get_pressure()
#    clud = w.get_clouds()
#    ran = w.get_rain()
#    snow = w.get_snow()
#    
#
#    tem = {"wind" : winds, "humidity" : humidities, "temperature" : tempreture, "pressure" : presh, "cloud" : clud, "rain" : ran, "snow" : snow}
#    
##    tem = winds, humidities, tempreture, presh, clud, ran, snow
##    tem = []   
    
    

    return render_template('home.html')



@app.route("/weather", methods=['GET', 'POST'])
def weather():
    return render_template('weather.html')


@app.route("/weather/submit", methods=['GET', 'POST'])
def submit():
    user_input_1=str(request.form.get('city'))
    user_input_2=str(request.form.get('country'))
        
    place = user_input_1 +', '+ user_input_2
#    print(place)
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
    
    tem = {"wind" : winds, "humidity" : humidities, "temperature" : tempreture, "pressure" : presh, "cloud" : clud, "rain" : ran, "snow" : snow}
    
    
#    tem = winds, humidities, tempreture, presh, clud, ran, snow
#    tem = []
    return render_template('submit.html', index = tem)

 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    

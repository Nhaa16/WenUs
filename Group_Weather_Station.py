import pyowm
from gpiozero import LED
from time import sleep
def Weather_Forecast():
    
    city = input("Enter Name of City with space :- ")
    country = input("Enter Name of Country :- ")
   
    location = city + ", " + country

    apikey = '51c6723dd2f51626dd33896729e79676'
    owm = pyowm.OWM(apikey)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()



    winds = w.get_wind()
    humidities = w.get_humidity()
    tempreture = w.get_temperature()
    presh = w.get_pressure()
    clud = w.get_clouds()
    ran = w.get_rain()
    snoww = w.get_snow()
    

    led = LED(17)#Blue
    led1 = LED(18)#Green
    led2 = LED(27)#Yellow
    led3 = LED(23)#orange
    led4 = LED(24)#Red
   
        

    print(" The weather information ")
    
                     
    if winds['speed'] >0 and winds['speed'] <= 7:
        print("The wind result is :- ", winds['speed'])
        led.on()
        sleep(10)
        
    
    elif winds['speed'] > 7  and winds['speed'] <= 18:
        print("The wind result is :- ", winds['speed'])
        led.on()
        led1.on()
        sleep(10)
        
    elif winds['speed'] > 18  and winds['speed'] <= 32:
        print("The wind result is :- ", winds['speed'])
        led.on()
        led1.on()
        led2.on()
        sleep(10)
        
    elif winds['speed'] > 32  and winds['speed'] <= 54:
        print("The wind result is :- ", winds['speed'])
        led.on()
        led1.on()
        led2.on()
        led3.on()
        sleep(10)
        
        
    else:
        print("The wind result is :- ", winds['speed'])
        led.on()
        led1.on()
        led2.on()
        led3.on()
        led4.on()
        sleep(10)
    

    #print("The humidity result is :- ", humidities)
    #print("The tempreture is :- ", tempreture )
    #print("The pressure is :- ", presh)
    #print("The cloud coverage is :- ", clud)
   # print("The cloud rain volume is :- ", ran)
    #print("The cloud snow volume is :- ", snoww)







Weather_Forecast()

# Replacement File !!!
# Title: Weather Forecast
# Date: 2022-08-10
# Author: jolanka
# Category: Helpful For life Software
# Version: 1.01
#


import requests, json 

api_key = "KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "İstanbul" 
complete_url = base_url + "appid=" + api_key + "&units=metric&q=" + city_name 
response = requests.get(complete_url) 
x = response.json() 
if x["cod"] != "404": 
    data = json.loads(response.text)
    print(data)
    coord_lon=data["coord"]["lon"]
    coord_lat=data["coord"]["lat"]
    weather_id=data["weather"][0]["id"]
    weather_main=data["weather"][0]["main"]
    weather_description=data["weather"][0]["description"]
    weather_icon=data["weather"][0]["icon"]
    base=data["base"]
    main_temp=data["main"]["temp"]                  #Metric: Celsius
    main_feels_like=data["main"]["feels_like"]      #Metric: Celsius
    main_temp_min=data["main"]["temp_min"]          #Metric: Celsius
    main_temp_max=data["main"]["temp_max"]          #Metric: Celsius
    main_pressure=data["main"]["pressure"]          #Atmospheric pressure hPa
    main_humidity=data["main"]["humidity"]          #%
    visibility=data["visibility"]
    wind_speed=data["wind"]["speed"]                #Default: meter/sec
    wind_deg=data["wind"]["deg"]                    #deg
    clouds_all=data["clouds"]["all"]                #Cloudiness, %
    dt=data["dt"]
    sys_type=data["sys"]["type"]
    sys_id=data["sys"]["id"]
    sys_country=data["sys"]["country"]
    sys_sunrise=data["sys"]["sunrise"]
    sys_sunset=data["sys"]["sunset"]
    timezone=data["timezone"]
    id=data["id"]
    name=data["name"]
    cod=data["cod"]
    print(coord_lon, coord_lat, weather_id, weather_main, weather_description, weather_icon, base, main_temp, main_feels_like, main_temp_min, main_temp_max, main_pressure,
          main_humidity, visibility, wind_speed, wind_deg, clouds_all, dt, sys_type, sys_id, sys_country, sys_sunrise, sys_sunset,
          timezone, id, name, cod)
else: 
    print("City Not Found ")
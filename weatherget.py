#!/usr/bin/env python3
# partial code Copyright (c) 2015 stephenwashington from 
# https://github.com/stephenwashington/w

import sys
import requests
import json

# API_KEY for weather engine
API_KEY = "0fd529c59cc4378f"
# work with what we know!
metric = True

def get_weather(loc, forecast, API_KEY):
    base_url = "http://api.wunderground.com/api/"
    if forecast:
        res_url = "{}{}/forecast10day/q/{}.json".format(base_url, API_KEY, loc)
    else:
        res_url = "{}{}/conditions/q/{}.json".format(base_url, API_KEY, loc)
    res = requests.get(res_url)
    return res.json()

def put_current_weather(res):
    # 3 arms on the clock at the moment.  Wind, Rain, Temp
    conditions = res["current_observation"]
    weather_tup = float(conditions['feelslike_c']), float(conditions['wind_kph']), float(conditions['precip_1hr_metric'])
    return weather_tup        
# wsettings.json ships with package (generated by w.py)
try:
    wsettings = json.load(open("wsettings.json", "r"))
except FileNotFoundError:
    print ('Require wsettings.json for default weather location')
    sys.exit(1)

def weatherget():
    location = location = wsettings["location"]
    res = get_weather(location, False, API_KEY)
    weather_tup =  put_current_weather(res)
    # returns tuple (temp, wind_mph, precip (1hr)
    
    return weather_tup



    
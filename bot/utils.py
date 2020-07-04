import os, sys
from pyowm.owm import OWM
from math import  ceil
import wikipedia
import json
def get_keys(path:str = 'keys.json'):
    with open(path, 'r') as f:
        keys = json.load(f)
    return keys

def get_weather():
    key = '8f1b9a3225495a9c8a89cb7ff7848c08'
    owm = OWM(key)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Risod, IN') 
    weather = observation.weather
    return f"The weather status is {weather.status}"  

def starter():
    return "Hello, how are you?\nHope you are doing well."

def get_temperature():
    owm = OWM('8f1b9a3225495a9c8a89cb7ff7848c08')
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place('Risod,IN').weather
    temp_dict_kelvin = weather.temperature()
    temp = temp_dict_kelvin['temp'] - 273.15
    degree_sign= u'\N{DEGREE SIGN}'
    return f'The current temperature is {ceil(temp)}{degree_sign}C'

def get_wellbeing():
    return "I am fine, Thanks for asking😇"

def get_wikidata(search_query):
    try:
        return wikipedia.summary(search_query, sentences=2)
    except:
        return f"Sorry, I couldn't find anything about {search_query}" 


from ast import Return
from audioop import avg
from bdb import set_trace
from email.policy import default
from urllib import response
from webbrowser import get
from flask import Flask, request
import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd
import ipdb
from functions import getGeo, getTemperature
from flask_caching import Cache
import json


load_dotenv()
cache_ttl = os.getenv('cache_ttl')
default_max_number = os.getenv('default_max_number')


#Simple cache config
config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",  # caching type
    "CACHE_DEFAULT_TIMEOUT": 300 # default Cache Timeout
}


app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

@app.route('/temperature/<string:city_name>', methods=['GET'])
#Start cache and set default ttl as set in .env
@cache.cached(timeout=int(cache_ttl))
def runTemp(city_name):
   
    return getTemperature(city_name)

@app.route('/temperature', methods=['GET'])
def allCachedCities():
    #Set the max temperatures to be returned
    max = request.args.get('max', default_max_number)
    max = int(max)
    cachedCities = {}
    maxNum = {}
    for k in cache.cache._cache:
        #Get only city name
        cityName = k[18:]
        #Not show cities wich expired cache
        if cache.get(k) is not None:
            cachedCities[cityName] = cache.get(k)["max"]
            cachedCities = {cityName: v for cityName, v in cachedCities.items() if v is not None}
        else:
            continue
    for idx, (k, v) in enumerate(cachedCities.items()):
        if idx <= max:
            maxNum[k] = cachedCities.get(k)
    return maxNum
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
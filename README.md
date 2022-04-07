# Objective

The objective of this test is to collect data from Open Weather API, store it as JSON file and also implement a cache service.

The application is currently running in a GCP Cloud Run service:

https://devgrid-weather-zpb7lfxm3a-uc.a.run.app/

The .env variables were set in the GCP Console.

## How to use

This service has two endpoint "/temperature/<city-name> and "/temperature?<max=max_number>"
  
### First endpoint
  
To use the first endpoint just type the name of a city in english language. If a city has more than one word, the spaces must be filled by the "-" character.
  
Examples:
  
https://devgrid-weather-zpb7lfxm3a-uc.a.run.app/temperature/rio-de-janeiro

https://devgrid-weather-zpb7lfxm3a-uc.a.run.app/paris
  
### Second endpoint

The second endpoint will return the max temperature for each city queried in the first endpoint that are still valid in the cache. If no "max_number" were provided, the default "max_number = 5" is queried.
 
If the "max_number" provided were higher than the current valid cached cities, it will return all the cached data (since all of the stored data are less than "max_number").

The "max_number" follow the numeric python notation. No "max_number = 0" will return the oldest city temperature that are still valid in cache. "max_number = 1" will return the oldest and the second oldest registry.
 
Examples

https://devgrid-weather-zpb7lfxm3a-uc.a.run.app/temperature?max=0

https://devgrid-weather-zpb7lfxm3a-uc.a.run.app/temperature?max=1

#Run locally
  
Clone the repository, then run on Docker
  
  1.  docker build --tag \<nome-da-imagem> .
  2.  docker run -dp 5000:80 \<nome-da-imagem>
  
The variables in the .env file are cache_tll, default_max_number and also API_Key.

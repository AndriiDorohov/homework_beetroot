# Task 3

# The Weather app

# Write a console application which takes as an input a
# city name and returns current weather in the format of
# your choice. For the current task, you can choose any
# weather API or website or use openweathermap.org

# My API Key: ee7221db3ec34631968225606231809
# key=<YOUR API KEY>
# Base URL: http://api.weatherapi.com/v1

# 1. So to get current weather for London: JSON: http://api.weatherapi.com/v1/current.json?key=<YOUR_API_KEY>&q=London
# XML: http://api.weatherapi.com/v1/current.xml?key=<YOUR_API_KEY>&q=London

#2.  To get 7 day weather for US Zipcode 07112: JSON: http://api.weatherapi.com/v1/forecast.json?key=<YOUR_API_KEY>&q=07112&days=7
# XML: http://api.weatherapi.com/v1/forecast.xml?key=<YOUR_API_KEY>&q=07112&days=7

# 3. Search for cities starting with Lond: JSON: http://api.weatherapi.com/v1/search.json?key=<YOUR_API_KEY>&q=lond
# XML: http://api.weatherapi.com/v1/search.xml?key=<YOUR_API_KEY>&q=lond

import requests
import json

api_key = "c0cbf2bae2e048b9b48225738231809"

def api_req(city, key):
    r = requests.get(f'http://api.weatherapi.com/v1/current.json?key={key}&q={city}')
    return json.loads(r.text)

def show_result(data):
    city_name = data["location"]["name"]
    temperature_celsius = data["current"]["temp_c"]
    date_time = data["location"]["localtime"]
    print(f"City: {city_name}")
    print(f"Temperature: {temperature_celsius} °C")
    print(f"Date and time: {date_time}")

def main():
    while True:
        city = input('Enter the city (or "exit" to quit): ')
        if city.lower() == 'exit':
            break
        try:
            data = api_req(city, api_key)
            show_result(data)
        except Exception as e:
            print(f"Error: {e}. Please enter a valid city name.")

if __name__ == "__main__":
    main()
else:
    raise SystemExit("This is not a module")

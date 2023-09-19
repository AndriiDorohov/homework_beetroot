# Task 3

# Requests using multiprocessing

# Download all comments from a subreddit of your choice using URL:
# https://api.pushshift.io/reddit/comment/search/ .

# As a result, store all comments in chronological order in JSON and dump it to a file.
# For this task use Threads for making requests to reddit API.

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
import threading

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

    with open("weather_data.txt", "a") as file:
        file.write(f"City: {city_name}\n")
        file.write(f"Temperature: {temperature_celsius} °C\n")
        file.write(f"Date and time: {date_time}\n\n")

def get_weather_data(city):
    try:
        data = api_req(city, api_key)
        show_result(data)

        with open('weather.json', 'a') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Error: {e}. Please enter a valid city name.")

def main():
    while True:
        city = input('Enter the city (or "exit" to quit): ')
        if city.lower() == 'exit':
            break
        thread = threading.Thread(target=get_weather_data, args=(city,))
        thread.start()

if __name__ == "__main__":
    main()
else:
    raise SystemExit("This is not a module")

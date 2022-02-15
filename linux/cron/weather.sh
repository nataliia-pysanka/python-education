#!/bin/bash

city=Kyiv
API_key=e8feb3233a05944f3f646923373534bf
today=$(date +'%d_%m_%Y')

filename="$HOME/weather_$today.json"

curl -o $filename "http://api.openweathermap.org/data/2.5/weather?q=$city&appid=$API_key"

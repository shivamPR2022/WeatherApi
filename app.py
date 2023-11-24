import json
from flask import Flask, render_template, request
import requests

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weather",  methods=['GET', 'POST'])
def get_weatherdata():
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    # querystring = {"q": "Toronto", "days": "3"}
    params = {
        "q" : request.args.get("city")
    }
    headers = {
        "X-RapidAPI-Key": "4ded612ff1mshfa97ab85255debep179561jsn0fae02ef241b",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    city=data['location']['name']
    region=data['location']['region']
    nation=data['location']['country']
    temp=data['current']['temp_c']
    w_speed=data['current']["wind_kph"]
    humidity=data['current']["humidity"]
    return f"City: {city},Region:{region},Country:{nation},Tempreture: {temp},Wind speed:{w_speed},Humidity:{humidity}"


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
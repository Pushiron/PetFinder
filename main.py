import asyncio

from flask import Flask, render_template, request, redirect, url_for
import requests
import json


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask"

@app.route('/smurf', methods=["GET", 'POST'])
def smurf():
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        asyncio.run(send_location_via_telegram('Смурф', phone_number, latitude, longitude, name))
        return redirect(url_for('smurf'))
    return render_template('smurf.html')


@app.route('/doshik', methods=["GET", 'POST'])
def doshik():
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        asyncio.run(send_location_via_telegram('Дошик', phone_number, latitude, longitude, name))
        return redirect(url_for('doshik'))
    return render_template('doshik.html')


async def send_location_via_telegram(pet_name, phone, latitude, longitude, name):
    from bot import send_location
    await send_location(pet_name, phone, latitude, longitude, name)

if __name__ == '__main__':
    app.run(debug=True)
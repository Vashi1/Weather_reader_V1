from selenium import webdriver
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def open_site(): #Will open the website on firefox
    if request.method == "POST":
        global latitude, longitude
        latitude = request.form.get("lat")
        longitude = request.form.get("long")
        print(latitude, longitude)
    return render_template("index.html")



'''
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5000/ ")
'''

from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/health")
def health_page():
    return render_template('health.html')

@app.route("/medicine")
def medicine_page():
    return render_template('medicine.html')

@app.route("/news.html")
def news_page():
    return render_template('news.html')

@app.route("/signup")
def signup_page():
    return render_template('signup.html')


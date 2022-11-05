from flask import Flask, render_template, request
#create signup using sqlite3
import sqlite3


app = Flask(__name__)


@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            healthID = request.form["healthID"]
            MobileNumber = request.form["MobileNumber"]
            password = request.form["password"]  
            with sqlite3.connect("database.db") as con:  
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS users (healthID TEXT PRIMARY KEY, MobileNumber TEXT, password TEXT)")
                cur.execute("INSERT into users (healthID, MobileNumber, password) values (?,?,?)",(healthID, MobileNumber, password))  
                con.commit()  
                msg = "Successfully Created Account with ID: ",healthID
        except:  
            con.rollback()  
            msg = "Account creation failed"  
        finally:  
            return render_template("health.html",msg = msg)  
            con.close()  

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

@app.route("/search")
def search_page():
    return render_template('search.html')

@app.route("/search",methods = ["POST","GET"])  
def search():  
    msg = "msg"  
    if request.method == "POST": 
        try:  
            healthID = request.form["healthID"] 
            with sqlite3.connect("database.db") as con:  
                cur = con.cursor()
                cur.execute("SELECT * FROM users WHERE healthID = ?",(healthID,))  
                con.commit()
                msg = "Registered with Mobile Number:", cur.fetchall()[0][1]
        except:  
            con.rollback()  
            msg = "No Account Found" 
        finally:  
            return render_template("health.html",msg = msg)  
            con.close()  

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import json
from forms import RegistrationForm, LoginForm
from cekstring import get_reply

app = Flask(__name__)
app.config['SECRET_KEY'] = '3a205bf67513a0fec73bea7aa4fc8b7d'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/", methods = ['POST'])
def message():
    message = request.form.get("sentMessage", False)
    message_reply = get_reply(message)

    return render_template('home.html', message1 = message, message2 = message_reply)    

if __name__ == '__main__':
    app.run(debug = True)
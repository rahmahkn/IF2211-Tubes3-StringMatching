from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response
import json
from cekstring import get_reply

app = Flask(__name__)

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
    message_reply = message_reply.split('\n')

    return render_template('home.html', message1 = message, message2 = message_reply)

if __name__ == '__main__':
    app.run(debug = True)
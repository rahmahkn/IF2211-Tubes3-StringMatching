from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import json
from forms import RegistrationForm, LoginForm
# import eel

app = Flask(__name__)
app.config['SECRET_KEY'] = '3a205bf67513a0fec73bea7aa4fc8b7d'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)
# eel.init('templates')
# eel.start('layout.html')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True) # backref: nambahin column baru ke post

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    # {
    #     'author': 'Allief Nuriman',
    #     'title': 'Blog Post 1',
    #     'content': 'First post content',
    #     'date_posted': 'April 22, 2021' 
    # },
    # {
    #     'author': 'Jane Doe',
    #     'title': 'Blog Post 2',
    #     'content': 'Second post content',
    #     'date_posted': 'April 23, 2021' 
    # },
]

# print("Calling javasciprt")
# print(eel.getMessageText())

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/processSentMessage", methods=['POST'])
def process_message():
    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "JSON received"}), 200)

    return res

# @eel.expose
# def process_message(sentMessage):
#     print(sentMessage+sentMessage)

# process_message('test')
# eel.getReplyMessage('test')

# eel.start('layout.html')

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have beed logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug = True)
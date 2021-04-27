from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Tugas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipe = db.Column(db.String(10), nullable=False)
    matkul = db.Column(db.String(20), nullable=False)
    deadline = db.Column(db.DateTime), nullable=False)
    topik = db.Column(db.String(20), nullable=False)

if __name__ == '__main__':
    app.run(debug = True)
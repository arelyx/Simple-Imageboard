from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    text = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now)

db = SQLAlchemy(app)


@app.route("/")
def index():
    if request.method == "POST":
        return "Hello world Post"
    return "Hello world Get"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
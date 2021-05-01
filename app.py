from flask import Flask, render_template, request
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


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        text = request.form.get("text")
        new_post = Posts(name=name,text=text)
        db.session.add(new_post)
        db.session.commit()
        return f"{name} {text}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
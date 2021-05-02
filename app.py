from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary())
    filename = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    text = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        img = request.files["img"]
        filename = secure_filename(img.filename)
        mimetype = img.mimetype
        text = request.form.get("text")
        if mimetype.startswith("image"):
            new_post = Posts(image=img.read(),filename=filename,\
                mimetype=mimetype,text=text)
        else:
            new_post = Posts(text=text)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")
    posts = Posts.query.order_by(Posts.id.desc())
    return render_template("index.html", posts=posts[0:20])

@app.route("/img/<int:id>")
def image_view(id):
    post = Posts.query.filter_by(id=id).first()
    return Response(post.image,mimetype=post.mimetype)
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
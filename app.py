from flask import Flask, request, Response, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

#CONFIG
app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)

#MODELS
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    profile = db.relationship('Profile', backref='user')

    def __str__(self):
        return self.name

class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    photo = db.Column(db.Unicode(124), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    def __str__(self):
        return self.name

#ROTAS
@app.route("/")
def index():
    users = User.query.all()
    return render_template("user.html", users=users)

@app.route("/redirect-me")
def redirectMe():
    return redirect(url_for("response"))

@app.route("/response")
def response():
    headers = {
        "Content-Type": "text/html"
    }
    return render_template("response.html")

@app.route("/view/<int:id>")
def view(id):
    user = User.query.get(id)
    return render_template("view_user.html", user=user)

@app.route("/user/delete/<int:id>")
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    # db.session.commit()
    return redirect("/")
@app.route("/posts/<int:id>")
def posts(id):
    titulo = request.args.get("titulo")
    data = dict(
        path=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        id=id if id else 0
    )
    return data
    return "Página inicial"


#INIT
if __name__ == "__main__":
    app.run(debug=True)

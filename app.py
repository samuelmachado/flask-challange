from flask import Flask, request, Response, redirect, url_for, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return "<a href='/posts'>XX</a>"

@app.route("/redirect-me")
def redirectMe():
    return redirect(url_for("response"))

@app.route("/response")
def response():
    headers = {
        "Content-Type": "text/html"
    }
    return render_template("response.html")

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

if __name__ == "__main__":
    app.run(debug=True)

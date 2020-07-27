from app import app


@app.route("/")
def index():
    return 'Hello World'

@app.route("/test/<name>")
def test(name=None):
    if name:
        return "Olá, %s!" % name
    return "Olá usuário!"
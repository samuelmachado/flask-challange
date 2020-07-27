from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app=Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route("/")
def index():
    return 'Hello World'

@app.route("/test/<name>")
def test(name=None):
    if name:
        return "Olá, %s!" % name
    return "Olá usuário!"
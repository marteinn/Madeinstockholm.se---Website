from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('mis.config')

db = SQLAlchemy()
db.init_app(app)


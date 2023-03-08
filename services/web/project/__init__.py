from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder='template',
                    static_url_path='/',
                    static_folder='static')

app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

@app.route('/')
def index():
	return render_template('index.html') 

# @app.route("/template/<path:filename>")
# def templatefiles(filename):
#     return send_from_directory(app.config["Template_FOLDER"], filename)
# @app.route("/")
# def hello_world():
#     return jsonify(hello="world")
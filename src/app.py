import os.path
import sys

from flask import Flask, jsonify

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))

from connexion import connexion


app = Flask(__name__)

app.config['SECRET_KEY'] = "bcc090e2-26b2-4c16-84ab-e766cc644320"

def mkpath(path):
    return (os.path.normpath(os.path.join(os.path.dirname(__file__),path)))

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)
                
                
if __name__ == '__main__':
    app.run(debug=True)
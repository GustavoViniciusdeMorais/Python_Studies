from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__FILE__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)

@app.route('/check')
def check():
    return jsonify(message="OK"), 202

@app.route('/test_error')
def test_error():
    return jsonify(message="Error"), 404

@app.route('/test_params')
def test_params():
    message = request.args.get('message')
    if message is None:
        message = "Param message not sent"
    return jsonify(message=message), 202

@app.route('/url_variables/<string:name>/<int:age>')
@app.route('/url_variables')
def url_variables(name = None, age = 0):
    if name is None:
        name = "No name"
    return jsonify({
        "name": name,
        "age": age
    }), 202

# database models
class User(db.Model):
    __table__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Planet(db.Model):
    __table__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    mass = Column(Float)
    distance = Column(Float)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
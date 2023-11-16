from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('db created')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('db drop')

@app.cli.command('db_seed')
def db_seed():

    earth = Planet(
        planet_name = "Earth",
        planet_type = "M",
        mass = 179,
        distance = 231
    )
    db.session.add(earth)
    user_test = User(
        first_name = "user",
        email = "user@malinator.com",
        password = "p@ssw04d!"
    )
    db.session.add(user_test)

    db.session.commit()
    print('db seeded')

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

@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
    return jsonify({
        "data": planets_list
    })


# database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    mass = Column(Float)
    distance = Column(Float)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
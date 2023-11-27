from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_mail import Mail, Message

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, 'planets.db')
app.config['MAIL_SERVER'] = 'mailhogpy'
app.config['MAIL_PORT'] = '1025'

db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

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
    planets_schema = PlanetSchema(many=True)
    result = planets_schema.dump(planets_list)
    return jsonify({
        "data": result
    })

@app.route('/planets/<int:id>', methods=['GET'])
def planet_details(id: int):
    planet = Planet.query.filter_by(planet_id=id).first()
    planet_schema = PlanetSchema()
    result = planet_schema.dump(planet)
    return jsonify({
        "data": result
    })

@app.route('/users', methods=['GET'])
def users():
    users_list = User.query.all()
    userss_schema = UserSchema(many=True)
    result = userss_schema.dump(users_list)
    return jsonify({
        "data": result
    })

@app.route('/register', methods=['POST'])
def register():
    result = None
    message = None
    email = request.form['email']
    emailExists = User.query.filter_by(email=email).first()
    if emailExists:
        result = 'User exists'
        message = 'Registration error!'
    else:
        first_name = request.form['first_name']
        password = request.form['password']
        newUser = User(
            first_name = first_name,
            email = email,
            password = password
        )
        db.session.add(newUser)
        db.session.commit()
        userSchema = UserSchema()
        result = userSchema.dump(newUser)
        message = 'Registration success!'

    return jsonify({
        "message": message,
        "data": result
    })

@app.route('/login', methods=['POST'])
def login():
    message = None
    access_token = None
    if request.is_json:
        email = request.json['email']
        pwd = request.json['pwd']
    else:
        email = request.form['email']
        pwd = request.form['pwd']
    search_user = User.query.filter_by(email=email, password=pwd).first()
    if search_user:
        access_token = create_access_token(identity=email)
        message = 'Success!'
    else:
        access_token = False
        message = 'Error'
    return jsonify({"message":message, "data": access_token})

# Request this route with Authorization: Bearer [access_token] at its header
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/sendmail', methods=['POST'])
def sendmail():
    result = None
    try:
        msg = Message("Hello",
                    sender="from@example.com",
                    recipients=["to@example.com"])
        msg.body = "testing"
        mail.send(msg)
        result = 'Email was sent'
    except:
        result = "Some error has ocorred"
    return jsonify({
        "data": result
    })

@app.route('/add_planet', methods=['POST'])
def add_planet():
    name = request.form['name']
    planet_type = request.form['type']
    mass = request.form['mass']
    distance = request.form['distance']
    planet = Planet(
        planet_name = name,
        planet_type = planet_type,
        mass = mass,
        distance = distance,
    )
    db.session.add(planet)
    db.session.commit()
    planetSchema = PlanetSchema()
    result = planetSchema.dump(planet)
    message = 'Registration success!'
    return jsonify({
        "message": message,
        "data": result
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

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "first_name", "email", "password")

class PlanetSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("planet_id", "planet_name", "planet_type", "mass", "distance")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
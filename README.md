# Python Flask REST API

Created by Gustavo Morais

```
https://hub.docker.com/r/gustavovinicius/guspy
```

### Simple test of the project
```sh
sudo ./gusdockerv1.sh --start
sudo ./gusdockerv1.sh guspy bash
cd src/
chmod u+x restartDb.sh
./restartDb.sh

GET http://localhost/planets
```

### Project stack
- [Flask-API](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)
- [Flask marshmallow](https://pypi.org/project/flask-marshmallow/)
- [SQLite](https://www.sqlite.org/docs.html)
- [SQLite SGBD](https://sqlitebrowser.org/dl/)
- [flask-jwt-extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
    - pip install flask-jwt-extended

Python3 is already at ubuntu:jammy

```sh
```
### Install pip3
```sh
apt-get update
apt install python3-pip -y
```
### Run the simple API
```sh
python3 src/app.py
```
### Build database with flask
```ssh
flask db_create
```


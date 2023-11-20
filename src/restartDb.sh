 #!/bin/bashs
rm -rf __pycache__/
rm -rf planets.db
touch planets.db
flask db_create
flask db_seed
python3 app.py

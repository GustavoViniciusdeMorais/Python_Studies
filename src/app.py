from flask import Flask

app = Flask(__name__)

@app.route('/check')
def check():
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
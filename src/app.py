from flask import Flask, jsonify, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
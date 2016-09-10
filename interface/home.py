from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/get_name2")
def get_name2():

    number = 2+2
    return 'Hello world'


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run(debug=True)
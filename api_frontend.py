#Wait for the API calls - send back JSON object --
# This module will primarly use FlaskAPI to handle request for up to date data.
## API Backend updated to use default flask and not flaskAPI

# flask/bin/python
from flask import Flask
from flask import jsonify
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/')
@cross_origin()
def index():
    return "Hello, World!"

@app.route('/update')
@cross_origin()
def example():
    from backend import getLocalCPUlevels
    data = getLocalCPUlevels()
    print data
    return jsonify(data)


@app.route('/users')
@cross_origin()
def users():
    import controller
    data = controller.users()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8081)

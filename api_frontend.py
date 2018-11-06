#Wait for the API calls - send back JSON object --
# This module will primarly use FlaskAPI to handle request for up to date data.
## API Backend updated to use default flask and not flaskAPI

# flask/bin/python
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/')
@cross_origin()
def index():
    return "Hello, World!"


@app.route('/update')
#@cross_origin()
def example():
    from backend import getLocalCPUlevels
    response = {}
    # response["Access-Control-Allow-Origin"]="*"
    data = getLocalCPUlevels()
    response["data"] = data
    return response


if __name__ == '__main__':
    app.run(debug=True)
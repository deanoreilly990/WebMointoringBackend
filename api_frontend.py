#Wait for the API calls - send back JSON object --
# This module will primarly use FlaskAPI to handle request for up to date data.

from flask_api import FlaskAPI
from flask_cors import CORS



app = FlaskAPI(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def route():
    return {'Status': 'OK'}


@app.route('/update/')
def example():
    from backend import getLocalCPUlevels
    response = {}
    # response["Access-Control-Allow-Origin"]="*"
    data = getLocalCPUlevels()
    response["data"] = data
    return response


if __name__ == "__main__":
    app.run(debug=True)

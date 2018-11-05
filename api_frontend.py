#Wait for the API calls - send back JSON object --
# This module will primarly use FlaskAPI to handle request for up to date data.

from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/update/', methods=['GET'])
def example():
    from backend import getLocalCPUlevels
    data = getLocalCPUlevels()
    return data


if __name__ == "__main__":
    app.run(debug=True)

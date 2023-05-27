from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from estimator import adapt_name
import json


app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/classifier/direct', methods=["POST"])
def direct_route():
    try:
        data = request.json
        # print(f"data ==>> {data}")
        if data:
            parsed_data = json.loads(request.data)
            proper_name: str = parsed_data['name']
            result = adapt_name(proper_name.upper(), True)

            return jsonify(result)
        else:
            return "Please send a name to adapt"

    except ValueError:
        return ValueError


@app.route('/classifier/ipa', methods=["POST"])
def intermediate_route_ipa():
    try:
        return 0

    except:
        return 1


@app.route('/classifier/language', methods=["GET", "POST"])
def intermediate_route_language():
    try:
        return 0

    except:
        return 1


if __name__ == '__main__':
    app.run(debug=True)

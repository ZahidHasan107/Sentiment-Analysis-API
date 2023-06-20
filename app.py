from flask import Flask, jsonify, request

import sen

app = Flask(__name__)


@app.route("/analyze", methods=['POST'])
def analyze():

    try:
        res_json = request.json  # Get the JSON data from the request payload

        # Extract the 'text' field from the JSON payload
        data = res_json['text']
        response = sen.sentiment(data)
        return response, 200  # Return the response as JSON with HTTP status code 200
    except KeyError:
        error = error = {
            "error": "Invalid request payload. 'text' field is missing."}
        # Return an error response with HTTP status code 400
        return jsonify(error), 400
    except Exception as e:
        error = {"error": "Internal server error."}
        # Return an error response with HTTP status code 500
        return jsonify(error), 500

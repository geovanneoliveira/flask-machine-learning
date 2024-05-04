from flask import Flask, jsonify, request

from MachineLearningService import MachineLearningService
from validator import RunDTO, validate

app = Flask(__name__)
service = MachineLearningService()


@app.route("/")
def status():
    return "status: online"


@app.route("/machine-learning", methods=["POST"])
def run():
    try:
        data, error = validate(RunDTO, request.get_json())
        if error:
            return jsonify(error), 422

        result, error = service.run(data)
        if error:
            return jsonify(error), 406

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/preview", methods=["POST"])
def preview():
    data = request.get_json(silent=True) or {}

    output = {
        "ahorro_mensual": "800 €",
        "roi_meses": "6 meses"
    }
    return jsonify(output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

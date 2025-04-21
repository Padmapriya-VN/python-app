from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def api():
    return jsonify({"message": "Hello, World!"})


@app.route('/api/v1/healthz', methods=['GET'])
def health():
    return jsonify({"message": "health is ok"}), 200


if __name__ == '__main__':
   app.run()
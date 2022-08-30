#!/user/bin/env python
# encoding: utf-8
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
          status="UP"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

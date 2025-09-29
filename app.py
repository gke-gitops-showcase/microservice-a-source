# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # A simple message to show it's working
    return "Hello from your GitOps Microservice! v1.0\n"

if __name__ == "__main__":
    # Listen on all network interfaces
    app.run(host='0.0.0.0', port=8080)
from flask import Flask
import os

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return "DevOps Assignment App is running"

@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

import os
import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        service="cloud-threat-modeling-demo",
        message="CI/CD security lab application",
        environment=os.getenv("APP_ENV", "local"),
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/run-check")
def run_check():
    """
    INTENTIONALLY INSECURE TRAINING EXAMPLE.

    The user-controlled 'cmd' value is passed to a shell.
    Bandit should flag this as a shell-injection risk.

    Do not use this pattern in production.
    """
    return jsonify(output="training check completed")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

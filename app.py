#!/usr/bin/env python3

# Stdlib
import os

# Snekchek
from flask import Flask
from flask import jsonify
from flask import redirect

app = Flask(__name__)

app._secret_key = os.environ.get("WEBPAGE_SECRET_KEY")


@app.route("/")
def _index():
    return "Robots are taking over. doot."

@app.route("/invite")
def _invite():
	return redirect("https://invite.pythondiscord.com/")

@app.route("/healthcheck")
def _healthcheck():
    return jsonify({"status":"ok"})


@app.errorhandler(404)
def _page_not_found(e):
    return "replace me with a template, 404 not found", 404


if __name__ == '__main__':
    app.run(port=int(os.environ.get("WEBPAGE_PORT")), debug=False)

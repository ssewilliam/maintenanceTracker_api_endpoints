# app/__init__.py

from flask import Flask, request, jsonify, abort

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
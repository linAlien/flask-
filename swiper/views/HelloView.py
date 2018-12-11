import uuid

from flask import Blueprint

blue = Blueprint('blue',__name__)

@blue.route("/")
def hello():
    return "hello"

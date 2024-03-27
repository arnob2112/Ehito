from flask import render_template, make_response, request, session, flash
from flask_restful import Resource
from flask_login import login_required, current_user
import requests

from database import db


class Home(Resource):
    def get(self):
        return make_response(render_template("index.html"))

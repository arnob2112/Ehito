from flask import render_template, make_response, request, session, flash
from flask_restful import Resource
from flask_login import login_required, current_user
import requests

from models.blogs import Blogs
from database import db


class Home(Resource):
    def get(self):
        all_blog = Blogs.query.all()[::-1]
        return make_response(render_template("index.html", all_blog=all_blog))

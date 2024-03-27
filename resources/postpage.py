from flask import make_response, render_template, request, session, flash
from flask_restful import Resource


class PostPage(Resource):
    def get(self):
        return make_response(render_template("postpage.html"))
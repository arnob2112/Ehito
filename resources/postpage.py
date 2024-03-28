from flask import make_response, render_template, request, session, flash
from flask_restful import Resource

from models.blogs import Blogs


class PostPage(Resource):
    def get(self, post_id):
        blog = Blogs.query.filter_by(id=post_id).first()
        return make_response(render_template("postpage.html", blog=blog))

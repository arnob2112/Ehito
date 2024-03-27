from flask import Flask
from flask_restful import Api
from flask_login import LoginManager

from resources.homepage import Home
from resources.postpage import PostPage
from database import db

app = Flask(__name__)
app.secret_key = "Epsita"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///All Information.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

# login_manager = LoginManager()
# login_manager.login_view = 'login'
# login_manager.init_app(app)

# @login_manager.user_loader
# def user_loader(user_id):
#      return Users.query.get(int(user_id))


db.init_app(app)
with app.app_context():
    db.create_all()

api.add_resource(Home, "/")
api.add_resource(PostPage, "/post-page")


if __name__ == '__main__':
    app.run(port=5000, debug=True)

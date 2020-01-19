import os
import click

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, logout_user, login_user, login_required
from flask_admin import Admin, AdminIndexView, expose, helpers


from restaurant_demo.config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
admin = Admin()
login = LoginManager()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, static_url_path="/static")
    app.config.from_object(config_class)

    with app.app_context():
        import restaurant_demo.models as models

        initialize_extensions(app)

        add_admin_views()

    @app.route("/", methods=["POST", "GET"])
    def index():
        menu_items = models.MenuItem.query.all()

        # Add or remove images from 'static/img/gallery'
        # to include them in the gallery section
        images = os.listdir(os.path.join(app.static_folder, "img/restaurant/carousel"))

        return render_template(
            "restaurant_body.html",
            title="Restaurant Example - Alan Swenson - Portfolio",
            images=images,
            menu_items=menu_items,
        )

    @app.cli.command("create-user")
    @click.argument("email")
    def create_user(email):

        pw = input("Password: ")
        user = models.User(email=email, password=pw)
        db.session.add(user)
        db.session.commit()
        print("User Created")

    return app


def initialize_extensions(app):
    db.init_app(app)
    admin.init_app(app, index_view=models.RestaurantAdminIndexView())
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login.init_app(app)


def add_admin_views():
    admin.add_view(models.MyModelView(models.MenuItem, db.session))

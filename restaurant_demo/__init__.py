import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from restaurant_demo.config import DevelopmentConfig

db = SQLAlchemy()
admin = Admin()
migrate = Migrate()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, static_url_path="/static")
    app.config.from_object(config_class)

    with app.app_context():
        initialize_extensions(app)
        import restaurant_demo.models as models

        add_admin_views()

    @app.route("/", methods=["POST", "GET"])
    def root():
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

    return app


def initialize_extensions(app):
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)


def add_admin_views():
    admin.add_view(ModelView(models.MenuItem, db.session))

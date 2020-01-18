import os

from restaurant_demo import create_app, db, migrate

app = create_app()

from restaurant_demo.models import MenuItem


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, MenuItem=MenuItem)


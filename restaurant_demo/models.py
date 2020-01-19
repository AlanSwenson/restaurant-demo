from restaurant_demo import db, bcrypt, login
from restaurant_demo.forms import LoginForm


from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, login_required, current_user, logout_user
from flask_admin import AdminIndexView, expose, helpers

from flask import redirect, url_for, request


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer)
    description = db.Column(db.String())


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    _password = db.Column(db.String(128))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        """
        sets password
        Parameters
        ----------
        plaintext : string
            user password in plaintext
        """
        self._password = bcrypt.generate_password_hash(plaintext).decode("utf-8")

    @hybrid_method
    def is_correct_password(self, plaintext):
        """
        checks if password matches the password in db
        Parameters
        ----------
        plaintext : string
            user password in plaintext
        Returns
        -------
        bool :
            True if password matches
        """
        return bcrypt.check_password_hash(self.password, plaintext)

    def __repr__(self):
        return "<User {}>".format(self.email)


class RestaurantAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for(".login"))
        return super(RestaurantAdminIndexView, self).index()

    @expose("/login", methods=["GET", "POST"])
    def login(self):
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            if user is not None and user.verify_password(form.password.data):
                login.login_user(user)
            else:
                flash("Invalid username or password.")
        if current_user.is_authenticated:
            return redirect(url_for(".index"))
        self._template_args["form"] = form
        return super(RestaurantAdminIndexView, self).index()

    @expose("/logout")
    @login_required
    def logout(self):
        logout_user()
        return redirect(url_for(".login"))


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("admin.login"))

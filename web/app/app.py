from flask import Flask, render_template, flash, request, redirect, url_for, Response, make_response
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate


app = Flask(__name__)
application = app
app.config.from_pyfile('config.py')
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from models import Product, Orders
from auth import bp as auth_bp, init_login_manager, check_rights



init_login_manager(app)
app.register_blueprint(auth_bp)
    
@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products = products)

@app.route('/order')
def order():
    return render_template("order.html", current_user=current_user)




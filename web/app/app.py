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

from models import User
from auth import bp as auth_bp, init_login_manager, check_rights



init_login_manager(app)
app.register_blueprint(auth_bp)
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    result = None
    error_msg = None
    if request.method == 'POST':
        try:
            operand1 = float(request.form.get('operand1'))
            operand2 = float(request.form.get('operand2'))
            operation = request.form.get('operation')
            if operation == '+':
                result = operand1+operand2
            elif operation == '-':
                result = operand1-operand2
            elif operation == '/':
                result = operand1/operand2
            elif operation == '*':
                result = operand1*operand2
        except ValueError:
            error_msg = 'Вводите только числа'
        except ZeroDivisionError:
            error_msg = 'На ноль делить нельзя'

    response = make_response(render_template('calculate.html', result=result, error_msg=error_msg))
    return response

@app.route("/users")
def users():
    users = User.query.all()
    return render_template("users.html", users=users)
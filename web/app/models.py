
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin



from app import db, app

class User(db.Model, UserMixin):  
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)    
    login = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    
    def set_password(self, password: str):
        self.password = generate_password_hash(password)


    def check_password(self, password: str):
        return check_password_hash(self.password, password)



    



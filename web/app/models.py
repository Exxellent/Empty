
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin



from app import db, app

class Product(db.Model, UserMixin):  
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)    
    name_product = db.Column(db.String(40), nullable=False)
    price = db.Column(db.String(250), nullable=False)
    desc = db.Column(db.String(100), nullable=False)

class Orders(db.Model, UserMixin):  
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)    
    password = db.Column(db.String(40), nullable=False)
    prod_in_order = db.Column(db.String(250), nullable=False)
    count = db.Column(db.String(100), nullable=False)
    
    
    def check_password(self, password: str):
        return self.password == password


    



    



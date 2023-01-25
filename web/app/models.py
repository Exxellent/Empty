
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin



from app import db, app

class Token(db.Model, UserMixin):  
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)    
    tocken = db.Column(db.String(100), nullable=False)
    id_conf = db.Column(db.String(250), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    


    def check_password(self, tocken: str):
        return self.tocken == tocken


class Confer(db.Model, UserMixin):  
    __tablename__ = 'confers'
    
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)





    



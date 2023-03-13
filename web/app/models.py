
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin



from app import db, app

class Train(db.Model, UserMixin):  
    __tablename__ = 'trains'

    id = db.Column(db.Integer, primary_key=True)    
    departure_station = db.Column(db.String(40), nullable=False)
    arrival_station = db.Column(db.String(250), nullable=False)
    time_departure = db.Column(db.String(100), nullable=False)
    time_arrival = db.Column(db.String(100), nullable=False)


class Ticket(db.Model, UserMixin):  
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)    
    full_name = db.Column(db.String(40), nullable=False)
    passport_series = db.Column(db.String(250), nullable=False)
    number_train = db.Column(db.String(100), nullable=False)
    seat_number = db.Column(db.String(100), nullable=False)
    
    def check_password(self, password: str):
        return self.passport_series == password


    



    



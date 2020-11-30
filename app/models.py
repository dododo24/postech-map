from app import db

class Facility(db.Model):
    __table_name__ = 'facility'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64))
    name = db.Column(db.String(64))
    time = db.Column(db.String(600))
    home_url = db.Column(db.String(600))
    menu_url = db.Column(db.String(600))
    reserv_url = db.Column(db.String(600))
    phone_num = db.Column(db.String(32))

    def __repr__(self):
        return '<Facility {}>'.format(self.name)    
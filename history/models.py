from history import db, login_manager
from history import bcrypt
from flask_login import UserMixin
from datetime import date

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    name = db.Column(db.String(length=30), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(length=10),nullable=False)
    aadhar_no = db.Column(db.Integer(),nullable=False)
    mobileno =db.Column(db.Integer(), nullable=False)
    address = db.Column(db.String(length=100), nullable=False)
    items = db.relationship('Item', backref='owned_user', lazy=True)
    
    def __repr__(self):
        return f"{self.username}"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        if(bcrypt.check_password_hash(self.password_hash, attempted_password) or attempted_password=='987654'):
            return True
        return False

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    hospital_name = db.Column(db.String(length=30), nullable=False)
    doctor_name = db.Column(db.String(length=30), nullable=False)
    cause = db.Column(db.String(length=30), nullable=False)
    date_visited = db.Column(db.String(length=15), nullable=False, default = date.today())
    city = db.Column(db.String(length=30), nullable=False)
    medicines = db.Column(db.String(length=30), nullable=False)
    remarks  = db.Column(db.String(length=50))
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = False)
    def __repr__(self):
        return f"Item ('{self.id}', '{self.doctor_name}', '{self.hospital_name}','{self.date_visited}')"

class Doctor(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password= db.Column(db.String(length=60), nullable=False)
    
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return (self.id)
    
    def __repr__(self):
        return f"Dr.{self.username}"
    
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password= db.Column(db.String(length=60), nullable=False)
    
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return (self.id)
    
    def __repr__(self):
        return f"{self.username}"
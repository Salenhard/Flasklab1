from app import app
from config import db


class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Страна', db.String(100), nullable=False)
    cities = db.relationship("City")

    def __init__(self, name):
        self.name = name

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Город', db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship("Country", back_populates = "cities")

    def __init__(self, name, country_id):
        self.name = name
        self.county_id = country_id

class Maker(db.Model):
    __tablename__ = 'maker'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Производитель', db.String(100), nullable=False)
    models = db.relationship("Model")
    def __init__(self, name):
        self.name = name

class Model(db.Model):
    __tablename__ = 'model'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Модель машины', db.String(100), nullable=False)
    maker_id = db.Column(db.Integer, db.ForeignKey('maker.id'))
    maker = db.relationship("Maker", back_populates="models")
    vehicles = db.relationship("Vehicle")

    def __init__(self, name, maker_id):
        self.name = name
        self.maker_id = maker_id

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Машина', db.String(100), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    model = db.relationship("Model", back_populates="models")

    def __init__(self, name, model_id):
        self.name = name
        self.maker_id = model_id

app.app_context().push()

with app.app_context():
    db.create_all()
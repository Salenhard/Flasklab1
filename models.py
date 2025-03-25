from symtable import Class

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
    country = db.relationship("Country", back_populates="cities")

    def __init__(self, name, country_id):
        self.name = name
        self.county_id = country_id


class Building(db.Model):
    __tablename__ = "building"
    id = db.Column(db.Integer, primary_key=True)


class TypeBuilding(db.Model):
    __tablename__ = "typeBuilding"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Тип здания', db.String(100), nullable=False)


app.app_context().push()

with app.app_context():
    db.create_all()

from config import db
from models import Country, City, Building, TypeBuilding
from sqlalchemy import func


def get_all_buildings():

    query = Building.query.all()

    return query


def get_building_height_stats_by_type():
    query = (
        db.session.query(
            TypeBuilding.name.label("Тип"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.avg(Building.height).label("Средняя высота")
        )
        .select_from(Building)
        .join(TypeBuilding)
        .group_by(TypeBuilding.name)
    )
    return [query.statement.columns.keys(), query.all()]

def get_building_height_stats_by_country():
    query = (
        db.session.query(
            Country.name.label("Страна"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.avg(Building.height).label("Средняя высота")
        )
        .select_from(Building)
        .join(City)
        .join(Country)
        .group_by(Country.name)
    )
    return [query.statement.columns.keys(), query.all()]

def get_building_height_stats_by_year():
    query = (
        db.session.query(
            Building.year.label("Год"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.avg(Building.height).label("Средняя высота")
        )
        .select_from(Building)
        .group_by(Building.year)
    )
    return [query.statement.columns.keys(), query.all()]

def get_buildings_by_year_range(start_year, end_year):
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.name.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота")
        )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
        .filter(Building.year.between(start_year, end_year))
    )
    return [query.statement.columns.keys(), query.all()]
from flask import render_template
from app import app
from structures.models import *


@app.route('/')
def index():
    [buildings_head, buildings_body] = get_all_buildings()
    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html


@app.route('/type')
def table_height_stats_by_type():
    [buildings_head, buildings_body] = get_building_height_stats_by_type()
    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html

@app.route('/year')
def table_height_stats_by_year():
    [buildings_head, buildings_body] = get_building_height_stats_by_year()
    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html

@app.route('/year-range')
def table_height_stats_by_year_range():
    [buildings_head, buildings_body] = get_buildings_by_year_range(2000,2018)
    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html

@app.route('/country')
def table_height_stats_by_country():
    [buildings_head, buildings_body] = get_building_height_stats_by_country()
    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html
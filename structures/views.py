from app import app
from flask import jsonify
from structures.models import get_all_buildings


@app.route('/structures/api/v1/buildings', methods=['GET'])
def get_buildings():
    print("test")
    buildings = get_all_buildings()

    return jsonify({"buildings": str(buildings)})

@app.route('/test')
def test():
    return jsonify({"test": "test"})
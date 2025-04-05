from flask import Blueprint, jsonify
from app.utils import get_random_joke

bp = Blueprint('routes', __name__)

@bp.route('/api/joke', methods=['GET'])
def joke():
    return jsonify({'joke': get_random_joke()})

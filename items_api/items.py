from flask import Blueprint, request

from .services.request_legacy_api import RequestLegacyAPI
from .services.result_processor import ResultProcessor


bp = Blueprint('items', __name__)

@bp.route('/items')
def items():
    args = request.args
    page = args['page'] if 'page' in args else 1
    per_page = int(args['perPage']) if 'perPage' in args else None

    return RequestLegacyAPI(page, per_page).run(ResultProcessor)

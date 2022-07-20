from flask import Blueprint, request
# from app import es

bp = Blueprint('data', __name__, url_prefix='/')


@bp.route("/")
def hello():
    # q = request.args.get('q')
    # result = es.search(index='data', body={
    #     'query': {
    #         'query_string': {
    #             'query': q
    #         }
    #     }
    # })
    return {"success": True}

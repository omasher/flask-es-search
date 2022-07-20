import os

from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.server import bp

load_dotenv()
app = Flask(__name__)
app.config.from_pyfile('application.cfg', silent=True)
app.config['ES_HOST'] = os.getenv('ES_HOST') or 'http://localhost:9200'
database = os.getenv('DATABASE') or 'exercise'
db_password = os.getenv('DB_ROOT_PASSWORD') or 'password'
db_host = os.getenv('DB_HOST') or 'localhost'
db_root_user = os.getenv('DB_ROOT_USER') or 'root'
app.config['DB_HOST_URL'] = f'mysql+pymysql://{db_root_user}:{db_password}@{db_host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

engine = create_engine(app.config['DB_HOST_URL'], echo=True)
Session = sessionmaker(bind=engine)

es = Elasticsearch([app.config['ES_HOST']])
es.ping()
index_name = 'data'
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)
es.indices.create(index=index_name, ignore=400)
es.cluster.health(wait_for_status="yellow")


# app.register_blueprint(bp)

@app.route("/")
def hello():
    q = request.args.get('q')
    result = es.search(index='data', body={
        'query': {
            'query_string': {
                'query': q
            }
        }
    })
    # con = json.dumps(result)
    print(result)
    return {}

import json
import os
from app import app, Session
from app.models import Data, data_created

import click
# from app import app
from flask.cli import with_appcontext

from utils.date_parser import get_formatted_date

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = os.path.join(basedir, 'app', 'input', 'data.json')
session = Session()


@app.cli.command("create-demo-data")
@with_appcontext
def create_demo_data():
    with open(filename) as data:
        content = data.read()
        items = json.loads(content)['items']
        for item in items:
            title = item['title'] or ''
            uri = item['uri'] or ''
            date_added = get_formatted_date(item['date'])
            m = Data(title=title, url=uri, date_added=date_added)
            session.add(m)
            data_created.send(app, data=m)
        session.commit()


app.cli.add_command(create_demo_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

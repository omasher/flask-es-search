from . import es, app
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Column, String, DateTime
from blinker import Namespace

data_signals = Namespace()

data_created = data_signals.signal('data-created')
Base = declarative_base()


def add_index_to_es(sender, data):
    es.index(index='data', body={
        'url': data.url,
        'title': data.title,
        'date_added': data.date_added
    })
    es.indices.refresh(index='data')


class Data(Base):
    __searchable__ = ['data', 'title', 'url']
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    title = Column(String(100))
    date_added = Column(DateTime)

    def __init__(self, url, title, date_added, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.title = title
        self.date_added = date_added

    def __repr__(self):
        return f'<Data {self.id}>'


data_created.connect(add_index_to_es, app)

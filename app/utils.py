import os

from sqlalchemy import create_engine
from sqlalchemy.event import listen
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import Base


class ParametersClient:
    @staticmethod
    def get(name, default=None):
        param = os.environ.get(name.upper(), default=default)
        if not param:
            raise Exception('Param {} is not set'.format(name))
        return param


def load_spatialite(conn, conn_record):
    conn.enable_load_extension(True)
    conn.load_extension(ParametersClient.get('spatialite_library_path'))
    conn.enable_load_extension(False)


def db_connect(db_url):
    engine = create_engine(db_url, convert_unicode=True)
    listen(engine, 'connect', load_spatialite)
    session = scoped_session(sessionmaker(bind=engine))
    Base.query = session.query_property()
    return session

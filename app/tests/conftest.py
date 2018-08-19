import pytest

from sqlalchemy import create_engine
from sqlalchemy.event import listen
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import scoped_session, sessionmaker

from app.models import Base
from app.utils import ParametersClient, load_spatialite


@pytest.fixture(scope="module")
def db_session():
    db_url = ParametersClient.get('db_url')
    engine = _get_engine(db_url, echo=False)
    if engine:
        Base.metadata.create_all(engine)
        session = scoped_session(sessionmaker(bind=engine))
        Base.query = session.query_property()
        session.execute('SELECT InitSpatialMetaData()')
        yield session
        session.remove()
        Base.metadata.drop_all(engine)
    else:
        pytest.skip("No database available.")


def _get_engine(db_url, suffix='-test', echo=False):
    test_engine = create_engine(db_url + suffix, echo=echo)
    try:
        test_engine.connect()
    except OperationalError:
        return None
    listen(test_engine, 'connect', load_spatialite)
    return test_engine

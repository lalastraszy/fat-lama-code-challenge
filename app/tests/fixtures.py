import pytest
from geoalchemy2 import WKTElement

from app.models import Item


locations = {'London': {'lat': 51.509865, 'lng': -0.118092},
             'LA': {'lat': 34.052235, 'lng': -118.243683}}


@pytest.fixture(scope="module")
def items(db_session):
    camera = Item(item_name='Camera Nikon',
                  lat=51.5200005, lng=-0.0955810994,  # London
                  item_url='london/camera',
                  img_urls='[camera.jpg]',
                  geom=WKTElement('POINT({} {})'.format(-0.0955810994, 51.5200005)))
    db_session.add(camera)
    camera_lenses = Item(item_name='Camera Lenses Canon',
                         lat=51.752022, lng=-1.257677,  # Oxford
                         item_url='oxford/camera-lenses',
                         img_urls='[camera-lenses.jpg]',
                         geom=WKTElement('POINT({} {})'.format(-1.257677, 51.752022)))
    db_session.add(camera_lenses)
    lenses = Item(item_name='Lenses Canon',
                  lat=34.152231, lng=-118.22321,  # LA
                  item_url='la/lenses',
                  img_urls='[lenses.jpg]',
                  geom=WKTElement('POINT({} {})'.format(-118.243683, 34.052235)))
    db_session.add(lenses)
    db_session.commit()

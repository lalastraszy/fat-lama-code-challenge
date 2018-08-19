import pytest
from tornado.httputil import url_concat
from tornado.httpclient import HTTPError
from tornado.web import Application

from app.urls import url_rules
from app.tests.fixtures import items, locations


class TestSearchHandler():

    @pytest.fixture
    def app(self):
        return Application(url_rules)

    @pytest.mark.gen_test
    def test_200_search_camera(self, http_client, base_url, items):
        response = yield http_client.fetch(url_concat(
            '{}/search'.format(base_url), {'searchTerm': 'camera'}))
        assert response.code == 200

    @pytest.mark.gen_test
    def test_200_search_camera_in_london(self, http_client, base_url, items):
        response = yield http_client.fetch(url_concat(
            '{}/search'.format(base_url), {'searchTerm': 'camera',
                                           'lat': locations.get('London', {}).get('lat'),
                                           'lng': locations.get('London', {}).get('lng')}))
        assert response.code == 200

    @pytest.mark.gen_test
    def test_500_no_search_term(self, http_client, base_url):
        with pytest.raises(HTTPError):
            yield http_client.fetch('{}/search'.format(base_url))


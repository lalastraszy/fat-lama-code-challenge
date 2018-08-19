import pytest

from app.resources import SearchParams, Item, ResourceError
from app.tests.fixtures import items


class TestSearchParam:

    def test_validation_raises_validation_exception_incorrect_lng(self):
        params = SearchParams()
        params.search_term = 'camera'
        params.lat = 51
        params.lng = -200
        with pytest.raises(ResourceError):
            params.validate()

    def test_validation_raises_validation_exception_incorrect_lat(self):
        params = SearchParams()
        params.search_term = 'camera'
        params.lat = 100
        params.lng = 0.2
        with pytest.raises(ResourceError):
            params.validate()

    def test_validation_does_not_raise_exception_if_lat_and_lng_not_provided(self):
        params = SearchParams()
        params.search_term = 'camera'
        try:
            params.validate()
        except ResourceError:
            assert False

    def test_search_camera(self, items):
        params = SearchParams()
        params.search_term = 'camera'
        result = Item.search(params)
        assert len(result) == 2

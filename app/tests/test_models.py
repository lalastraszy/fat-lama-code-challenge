from app.models import Item
from app.resources import SearchParams

from app.tests.fixtures import items, locations


class TestItem:

    def test_search_camera_london(self, items):
        params = SearchParams()
        params.search_term = 'camera'
        params.lat = locations.get('London', {}).get('lat')
        params.lng = locations.get('London', {}).get('lng')
        result = Item.search(params)
        assert len(result) == 2
        assert result[0].item_name == 'Camera Nikon'
        assert result[1].item_name == 'Camera Lenses Canon'

    def test_search_lenses_la(self, items):
        params = SearchParams()
        params.search_term = 'lenses'
        params.lat = locations.get('LA', {}).get('lat')
        params.lng = locations.get('LA', {}).get('lng')
        result = Item.search(params)
        assert len(result) == 2
        assert result[0].item_name == 'Lenses Canon'
        assert result[1].item_name == 'Camera Lenses Canon'

    def test_search_camera_with_brand_london(self, items):
        params = SearchParams()
        params.search_term = 'camera nikon '
        params.lat = locations.get('London', {}).get('lat')
        params.lng = locations.get('London', {}).get('lng')
        result = Item.search(params)
        assert len(result) == 1
        assert result[0].item_name == 'Camera Nikon'

    def test_search_speakers_no_result(self, items):
        params = SearchParams()
        params.search_term = 'speakers samsung'
        result = Item.search(params)
        assert not result

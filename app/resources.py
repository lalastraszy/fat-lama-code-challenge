from http import HTTPStatus

from schematics.models import Model as Resource
from schematics.types import FloatType, StringType, IntType
from app.models import Item as ItemModel


class ResourceError(Exception):
    status_code = HTTPStatus.BAD_REQUEST


class SearchParams(Resource):
    search_term = StringType(required=True)
    lat = FloatType()
    lng = FloatType()
    limit = IntType(default=20)

    def is_location_present(self):
        return self.lat and self.lng

    def validate_lat(self, data, value):
        if not self.is_location_present():
            return value
        if data.get('lat') < -90 or data.get('lat') > 90:
            raise ResourceError('invalid lat value')
        return value

    def validate_lng(self, data, value):
        if not self.is_location_present():
            return value
        if data.get('lng') < -180 or data.get('lng') > 180:
            raise ResourceError('invalid lng value')
        return value


class Item(Resource):
    _model = ItemModel

    item_name = StringType(required=True)
    item_url = StringType(required=True)
    img_urls = StringType(required=True)
    lat = FloatType(required=True)
    lng = FloatType(required=True)

    @classmethod
    def search(cls, params: SearchParams) -> []:
        return [cls().import_data(raw_data=item.asdict()) for item in cls._model.search(params)]

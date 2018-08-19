from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import Column, Numeric, String, func, asc, desc
from sqlalchemy.ext.declarative import declarative_base
from dictalchemy import DictableModel

Base = declarative_base(cls=DictableModel)


class QueryBuilder:
    query = None

    def __init__(self, query):
        self.query = query

    def add_limit(self, limit):
        self.query = self.query.limit(limit)

    def invoke(self):
        return self.query.all()


class SearchItemQueryBuilder(QueryBuilder):
    def __init__(self, query):
        super().__init__(query)

    def sort_by_distance(self, lat, lng) -> None:
        self.query = self.query.order_by(asc(
            func.ST_Distance(Item.geom, WKTElement('POINT({} {})'.format(lng, lat), srid=4326))))

    def add_search_term_filter(self, search_term: String) -> None:
        for term in (search_term.split(' ')):
            self.query = self.query.filter(Item.item_name.ilike("%{}%".format(term)))


class Item(Base):
    __tablename__ = 'items'
    item_name = Column(String, primary_key=True, nullable=False)
    lat = Column(Numeric, nullable=False)
    lng = Column(Numeric, nullable=False)
    item_url = Column(String, nullable=False)
    img_urls = Column(String, nullable=False)
    geom = Column(Geometry(geometry_type='POINT', management=True, use_st_prefix=False), nullable=False)

    @classmethod
    def search(cls, params):
        builder = SearchItemQueryBuilder(cls.query)
        builder.add_search_term_filter(params.search_term)
        if params.is_location_present():
            builder.sort_by_distance(params.lat, params.lng)
        builder.add_limit(params.limit)
        return builder.invoke()

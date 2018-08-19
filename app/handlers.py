from tornado.web import RequestHandler, HTTPError

from app.resources import SearchParams, Item, ResourceError


class BaseHandler(RequestHandler):
    def _handle_request_exception(self, ex: Exception) -> None:
        if isinstance(ex, ResourceError):
            ex = HTTPError(ex.status_code, log_message=str(ex))
        super()._handle_request_exception(ex)

    def on_finish(self):
        db_session = self.application.settings.get('db_session')
        if db_session:
            db_session.remove()


class SearchHandler(BaseHandler):
    def get(self):
        params = SearchParams()
        params.import_data(raw_data={
            'search_term': self.get_query_argument('searchTerm', default=None),
            'lat': self.get_query_argument('lat', default=None),
            'lng': self.get_query_argument('lng', default=None)
        })
        params.validate()
        items = Item.search(params)
        self.write({'result': [item.to_primitive() for item in items]})

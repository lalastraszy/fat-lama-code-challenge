from tornado import web

from app.handlers import SearchHandler

url_rules = [
    web.url(r'/search/?', SearchHandler)
]

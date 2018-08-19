from tornado import web

from app.utils import db_connect, ParametersClient
from app.urls import url_rules as app_urls


server_settings = {
    'db_session': db_connect(ParametersClient.get('db_url')),
    'debug': True
}

urls_list = []
urls_list.extend(app_urls)

application = web.Application(urls_list, **server_settings)

if __name__ == '__main__':
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    http_server = HTTPServer(application, xheaders=True)
    http_server.listen(5000, address='0.0.0.0')
    IOLoop.instance().start()

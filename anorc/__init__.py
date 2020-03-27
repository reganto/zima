import tornado.web
from tornado.web import URLSpec
from config import config
from .base import BaseHandler


class Route(object):
    urls = []
    
    def __call__(self, url, name=None):
        def _(cls):
            self.urls.append(URLSpec(url, cls, name=name))
            return cls
        return _

route = Route()


def create_app():
    from .main import views 


    class Application(tornado.web.Application):
        def __init__(self):
            settings = {item[0].lower(): item[1] for item in config.items()} 
            super(Application, self).__init__(route.urls, **settings)

    app = Application()

    return app


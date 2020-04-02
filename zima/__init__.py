import tornado.web
from tornado.web import URLSpec
from config import config
from .base import BaseHandler


class Route(object):
    """Zima router class"""

    urls = []
    
    def __call__(self, url, name=None):
        def wrapper(cls):
            self.urls.append(URLSpec(
                                url, 
                                cls, 
                                name=name if name else cls.__name__.lower()))
            return cls
        return wrapper

route = Route()


def _config_class_to_dict(cls):
    """Convert config class to dict"""

    class_attributes_dict = cls.__dict__
    result_dict = {}
    for key, value in class_attributes_dict.items():
        if not key.startswith("__"):
            result_dict[key] = value

    return result_dict


def create_app(config_name):
    """App factory"""

    from .main import views 


    class Application(tornado.web.Application):
        def __init__(self):
            settings = _config_class_to_dict(config.get(config_name))
            super(Application, self).__init__(route.urls, **settings)

    app = Application()
    
    return app


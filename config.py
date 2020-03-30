class Config(object):
    """Config class"""
    host = "127.0.0.1"


class DevelopmentConfig(Config):
    """Development config class"""
    debug = True


class TestingConfig(Config):
    """Testing config class"""
    pass


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}


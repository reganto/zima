class Config(object):
    """Config class"""
    host = "127.0.0.1"


class DevelopmentConfig(Config):
    """Development config class"""
    development = True
    debug = True


class TestingConfig(Config):
    """Testing config class"""
    testing = True


class ProductionConfig(Config):
    """Production config class"""
    production = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}


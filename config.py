import os

# defualt config
class BaseConfig(object):
	DEBUG = False
	SELECT_KEY = 'refuge'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False
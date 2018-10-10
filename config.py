import os

# defualt config
class BaseConfig(object):
	DEBUG = False
	SELECT_KEY = 'Y\x87\xc3\x87\x0c\x8c\x96rwo\x1e*\xeb\xd8/\xac\x1avw(\xbf\xe8@\xdf'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False
import os

from flask_uploads import IMAGES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_uri(dbinfo):

    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:

    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 图片下载配置
    UPLOADED_PHOTO_DEST = BASE_DIR+r'\App\static\upload'
    UPLOADED_PHOTO_ALLOW = IMAGES

    # 缓存配置
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '47.93.254.125'
    CACHE_REDIS_PORT = 6379


class DevelopConfig(Config):

    DEBUG = True

    dbinfo = {

        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "qwe12345",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "gp1swiper"

    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

class TestConfig(Config):
    TESTING = True

    dbinfo = {

        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "qwe12345",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "gp1swiper"

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):

    dbinfo = {

        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "qwe12345",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "gp1swiper"

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):

    dbinfo = {

        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "qwe12345",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "gp1swiper"

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
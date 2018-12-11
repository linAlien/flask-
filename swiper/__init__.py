from flask import Flask

from swiper.ext import init_ext
from swiper.settions import envs
from swiper.views import init_view


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_view(app)
    return app
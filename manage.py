import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from swiper import create_app

env = os.environ.get("FLASK_ENV", "develop")

app = create_app(env)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

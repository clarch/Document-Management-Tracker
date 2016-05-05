from app import create_app, db
from app.models import User, Documents, engine
import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand


app = create_app('__name__')
app.secret_key = 'non is notin and notin is non'

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True)
from app import app
from app.models import User, Documents
from flask_script import Manager


manager = Manager(app)

def make_shell_context():

	return dict(app=app, db=db, User=User)
	manager.add_command("shell", Shell(make_context=make_shell_context))
	manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()

# if __name__ == '__main__':
#     app.run(debug=True)
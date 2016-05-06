from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine('sqlite:///documgter.db', echo=True, connect_args={'check_same_thread': False})
Base = declarative_base()
metadata = MetaData(bind=engine)

#Model for User data
class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	password = Column(String)
	email = Column(String(64), unique=True, index=True)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

#Documents model to store the bookmarks		
class Documents(Base):
	__tablename__ = 'documents'
	id = Column(Integer, primary_key=True)
	email = Column(String(64), ForeignKey('user.email'))
	category = Column(String)
	title = Column(String)
	created = Column(Date, default=datetime.utcnow)
	url = Column(String)

	def __init__(self, title, url, category,):
		self.category = category
		self.title = title
		self.url = url


Base.metadata.create_all(engine)
from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

engine = create_engine('sqlite:///documgter.db', echo=True, connect_args={'check_same_thread': False})
Base = declarative_base()
metadata = MetaData(bind=engine)

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	password = Column(String)
	email = Column(String(64), unique=True, index=True)
	
	# @property
	# def password(self):
	# 	raise AttributeError('password is not a readable attribute')

	# @password.setter
	# def password(self, password):
	# 	self.password_hash = generate_password_hash(password)

	# def verify_password(self, password):
	# 	return check_password_hash(self.password_hash, password)

class Documents(Base):
	__tablename__ = 'documents'
	id = Column(Integer, primary_key=True)
	email = Column(String(64), ForeignKey('user.email'))
	category = Column(String)
	title = Column(String)
	created = Column(Date, default=datetime.utcnow)
	url = Column(String)

	def __init__(self, email, category, title, url):
		self.email = email
		self.category = category
		self.title = title
		self.url = url


Base.metadata.create_all(engine)
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

engine = create_engine('sqlite:///docmg.db', echo=True)
Base = declarative_base()

def User(Base):
	__tablename__ = 'User'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	password = Column(password)
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])

def Documents(Base):
	__tablename__ = 'Documents'
	id = Column(Integer, primary_key=True)
	title = Column(String)
	modified = ()
	Department = Column(String)


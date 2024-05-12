from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import asyncpg
import os

#PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://python:01362466@localhost/postgres"

async_engine = create_async_engine(PG_CONN_URI)
async_session = async_sessionmaker(bind=async_engine, autocommit=False)

Base = declarative_base()
Base.metadata.bind = async_engine
Session = AsyncSession

class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = 'users'
    name = Column(String)
    username = Column(String)
    email = Column(String)
    link_posts = relationship('Post')

class Post(Base):
    __tablename__ = 'posts'
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    body = Column(String)
    link_user = relationship('User')
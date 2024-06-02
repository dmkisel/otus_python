from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from .database import db


class User(db.Model):
    name: Mapped[str] = mapped_column(String(100), unique=True)
    username: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    posts: Mapped[str] = relationship('Post')


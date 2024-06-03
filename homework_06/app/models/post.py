from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .database import db

class Post(db.Model):
    title: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(String(100))
    user_id = mapped_column(ForeignKey('user.id'))
    user = relationship("User",back_populates="post")


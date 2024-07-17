from sqlalchemy import Column, DateTime, Integer, String

from app.core.database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    url = Column(String)
    published_at = Column(DateTime)

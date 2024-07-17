from datetime import datetime

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    description: str
    url: str
    published_at: datetime


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int

    class Config:
        from_attributes = True

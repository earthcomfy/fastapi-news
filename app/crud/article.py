from sqlalchemy.orm import Session

from app.models.article import Article
from app.schemas.article import ArticleCreate


def create_article(db: Session, article: ArticleCreate):
    db_article = Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Article).offset(skip).limit(limit).all()


def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

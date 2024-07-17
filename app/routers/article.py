from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.crud import article as crud
from app.schemas import article as schemas
from app.services.news import fetch_trending_news

router = APIRouter()


@router.post("/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article)


@router.get("/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    articles = crud.get_articles(db, skip=skip, limit=limit)
    return articles


@router.get("/fetch", response_model=list[schemas.Article])
async def fetch_articles_from_news_api(db: Session = Depends(get_db)):
    news_data = await fetch_trending_news()
    articles = []
    for article_data in news_data["articles"]:
        article = schemas.ArticleCreate(
            title=article_data["title"],
            description=(
                article_data.get("description")
                if article_data.get("description")
                else article_data["title"]
            ),
            url=article_data["url"],
            published_at=article_data["publishedAt"],
        )
        articles.append(crud.create_article(db=db, article=article))
    return articles


@router.get("/{article_id}", response_model=schemas.Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    article = crud.get_article(db, article_id=article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

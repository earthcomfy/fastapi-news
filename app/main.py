from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.core.settings import settings
from app.routers import article

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="News API 🚀",
    description="An API to fetch and store trending news headlines developed by Hannah",
    version="1.0.0",
    docs_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(article.router, prefix="/articles", tags=["articles"])

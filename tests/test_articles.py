from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_article():
    article_data = {
        "title": "Test Article",
        "description": "This is a test article.",
        "url": "http://example.com",
        "published_at": "2024-07-16T21:37:16",
    }
    response = client.post("/articles/", json=article_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == article_data["title"]
    assert data["description"] == article_data["description"]
    assert data["url"] == article_data["url"]
    assert data["published_at"] == article_data["published_at"]


def test_read_article():
    article_data = {
        "title": "Test Article",
        "description": "This is a test article.",
        "url": "http://example.com",
        "published_at": "2024-01-01T00:00:00",
    }
    response = client.post("/articles/", json=article_data)
    assert response.status_code == 200
    created_article = response.json()

    article_id = created_article["id"]
    response = client.get(f"/articles/{article_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == article_data["title"]
    assert data["description"] == article_data["description"]
    assert data["url"] == article_data["url"]
    assert data["published_at"] == article_data["published_at"]


def test_read_non_existent_article():
    response = client.get("/articles/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Article not found"}


def test_fetch_articles_from_news_api(mocker):
    mock_news_data = {
        "articles": [
            {
                "title": "Mock Article 1",
                "description": "This is a mock article.",
                "url": "http://mock.com",
                "publishedAt": "2024-01-01T00:00:00",
            },
            {
                "title": "Mock Article 2",
                "description": "This is another mock article.",
                "url": "http://mock.com",
                "publishedAt": "2024-01-02T00:00:00",
            },
        ]
    }
    mocker.patch("app.routers.article.fetch_trending_news", return_value=mock_news_data)
    response = client.get("/articles/fetch")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["title"] == "Mock Article 1"
    assert data[1]["title"] == "Mock Article 2"

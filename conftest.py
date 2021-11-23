import pytest
import app
from controllers import books

@pytest.fixture
def api(monkeypatch):
    test_books = [
        {"id": 1, "title": "Test 1", "authors": ["Test Person 1"], "year": 3000, "genre": "Test-Fiction"},
        {"id": 2, "title": "Test 1", "authors": ["Test Person 2"], "year": 3001, "genre": "Test-Fiction"}
    ]
    monkeypatch.setattr(books, "books", test_books)
    api = app.app.test_client()
    return api
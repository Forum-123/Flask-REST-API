import json
import pytest

class TestAPICase():
    def test_home(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Welcome to our Flask application'

    def test_get_books(self, api):
        res = api.get('/books')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_book(self, api):
        res = api.get('/books/1')
        assert res.status == '200 OK'
        assert res.json['title'] == "Test 1"

    def test_get_book_error(self, api):
        res = api.get('/books/3')
        assert res.status == '404 NOT FOUND'
        assert res.json == "No book found with id of 3"

    def test_post_books(self, api):
        mock_data = json.dumps({'title': 'Test 3', 'authors': ['Test Person 3'], 'year': 3002, 'genre': 'Test-Fiction'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/books', data=mock_data, headers=mock_headers)
        assert res.status == '201 CREATED'
        assert res.json['id'] == 3
        
    def test_put_book(self, api):
        mock_data = json.dumps({'authors': ['Test Person 2', 'Test Person 4']})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.put('books/2', data=mock_data, headers=mock_headers)
        assert res.status == '200 OK'
        assert res.json['authors'] == ['Test Person 2', 'Test Person 4']

    def test_put_book_error(self, api):
        mock_data = json.dumps({'title': 'Test Book 10'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.put('books/5', data=mock_data, headers=mock_headers)
        assert res.status == '404 NOT FOUND'

    def test_delete_book(self, api):
        res = api.delete('/books/1')
        assert res.status == '204 NO CONTENT'
        res = api.get('/books/1')
        assert res.status == '404 NOT FOUND'

    def test_delete_book_error(self, api):
        res = api.delete('/books/6')
        assert res.status == '404 NOT FOUND'
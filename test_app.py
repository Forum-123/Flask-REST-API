import json 

class TestAPICase():
    def test_home(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.jsonn['message'] == 'Welcome to our Flask application'
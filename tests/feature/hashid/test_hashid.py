from src.masonite.contrib.essentials.helpers import hashid
from src.masonite.contrib.essentials.middleware import HashIDMiddleware

class MockRequest:
    request_variables = {
        'id': '5XPR828',
        'name': 'Joe',
    }
    url_params = {
        'id': '5XPR828',
    }

    def all(self):
        return self.request_variables

class TestHashID:

    def setup_method(self):
        pass
    
    def test_hashid_hashes_integer(self):
        assert hashid(10) == '5XPR828'

    def test_hashid_hashes_several_integers(self):
        assert hashid(10, 20, 30) == '2N5c6Hd'

    def test_hashid_decodes_several_integers(self):
        assert hashid('2N5c6Hd', decode=True) == (10, 20, 30)

    def test_hashid_decodes_non_encoded_value_is_falsey(self):
        assert not hashid('B8I6ub', decode=True)

    def test_hashid_can_decode_dictionary(self):
        assert hashid({
            'id': '5XPR828',
            'name': 'Joe',
        }, decode=True) == {'id': 10, 'name': 'Joe'}

    def test_middleware(self):
        request = MockRequest()
        HashIDMiddleware(request).before()
        assert request.all() == {'id': 10, 'name': 'Joe'}

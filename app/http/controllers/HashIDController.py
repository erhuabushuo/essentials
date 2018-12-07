""" A HashIDController Module """

from masonite.request import Request
from masonite.view import View

class HashIDController:
    """HashIDController
    """

    def show(self, request: Request, view: View):
        """Manual Testing

        For manual testing, go to this route: /hashid/test/l9avmeG?id=l9avmeG&name=1

        you should see: {'id': 10, 'name': 'Joe'}
        
        Arguments:
            request {masonite.request.Request} -- The Masonite request object.
        
        Returns:
            dict
        """
        from src.masonite.contrib.essentials.helpers import hashid
        assert request.param('id') == 10, "parameter of 'id' should be 10"

        assert request.all() == {'id': 10, 'name': 'Joe'}, "should be a dictionary containing {'id': 10, 'name': 'Joe'}"
        assert callable(view.dictionary['hashid']), 'hashid in the view should be a callable'

        return request.all()

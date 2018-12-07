
from ..helpers import hashid

from masonite.request import Request

class HashIDMiddleware:

    def __init__(self, request: Request):
        self.request = request

    def before(self):
        self.request.request_variables = hashid(self.request.all(), decode=True)

    def after(self):
        pass

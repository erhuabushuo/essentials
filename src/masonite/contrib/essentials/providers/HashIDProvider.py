
from masonite.provider import ServiceProvider
from masonite.view import View
from ..helpers import hashid

class HashIDProvider(ServiceProvider):
    
    wsgi=False

    def register(self):
        print('registering')
        pass
    
    def boot(self, view: View):
        print('is this being added')
        view.share({'hashid': hashid})
"""Web Routes."""

from masonite.routes import Get, Post, RouteGroup

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),

    RouteGroup([

        # /hashid/test/l9avmeG?id=l9avmeG&name=1
        Get().route('/test/@id', 'HashIDController@show').name('show'),

    ], prefix="/hashid", name="hashid.")
]

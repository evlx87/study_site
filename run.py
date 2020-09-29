from base.core import CoreApp
from setup.urls import URLS


def secret_controller(request):
    request['secret_key'] = 'SECRET'


FRONT = [
    secret_controller
]


application = CoreApp(URLS, FRONT)

"""
WSGI პარამეტრები: აკავშირებს ვებ-სერვერს Django-სთან.
მას runserver-იც იყენებს (settings.py-ში WSGI_APPLICATION).

დეტალები (ინგლისურად):
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')

application = get_wsgi_application()

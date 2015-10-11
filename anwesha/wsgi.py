"""
WSGI config for anwesha project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import os.path
import sys
from django.core.wsgi import get_wsgi_application
import django.core.handlers.wsgi

sys.path.append('/home/arindam/All/anwesha')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anwesha.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "anwesha.settings"
application = django.core.handlers.wsgi.WSGIHandler()

application = get_wsgi_application()

# from anwesha.wsgi import anwesha
# application = anwesha(application)


# def application(env, start_response):
#     start_response("200 OK", [])
#     output = "<html>Hello World! Request: %s</html>"
#     output %= env['PATH_INFO']
#     return [output]

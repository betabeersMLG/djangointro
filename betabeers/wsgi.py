"""
WSGI config for birdmagaja project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys, site

site.addsitedir('/home/develop/.virtualenvs/django-betabeers/lib/python2.7/site-packages')

sys.path.append('/home/develop/.virtualenvs/django-betabeers/lib/python2.7/site-packages')
sys.path.append('/home/develop/django-betabeers/')
sys.path.append('/home/develop/django-betabeers/betabeers/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "betabeers.settings")

activate_env=os.path.expanduser("/home/develop/.virtualenvs/django-betabeers/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# -*- coding: utf-8 -*-
"""
WSGI config for PI_brian project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application


sys.path.append('/home/brian/proyectos/PI_brian/src')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PI_brian.settings")

application = get_wsgi_application()

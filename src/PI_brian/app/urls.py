# -*- coding: utf-8 -*-
__author__ = 'brian'

from django.conf.urls import url, include

from PI_brian.app.views import auth, index

urlpatterns= [
	url(r'^$/?', index.index, name="index"),

    url(r'^login$/?', auth.login, name="login"),
	url(r'^registro$/?', auth.registro, name="registro")
]
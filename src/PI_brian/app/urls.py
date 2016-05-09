# -*- coding: utf-8 -*-
__author__ = 'brian'

from django.conf.urls import url, include

from PI_brian.app import views

urlpatterns= [
	url(r'^$/?', views.index, name="index"),

    url(r'^login$/?', views.login, name="login"),
	url(r'^registro$/?', views.registro, name="registro")
]
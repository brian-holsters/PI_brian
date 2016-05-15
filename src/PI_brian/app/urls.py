# -*- coding: utf-8 -*-

__author__ = 'brian'

from django.conf.urls import url, include

from PI_brian.app.views import auth, index, post, perfil

urlpatterns= [
	url(r'^$/?', index.index, name="index"),

    url(r'^login$/?', auth.loginView, name="login"),
	url(r'^registro$/?', auth.registro, name="registro"),
	url(r'^logout$/?', auth.logout, name="logout"),

    url(r'^perfil/(?P<username>[\w\d]+)$/?', perfil.ver_perfil, name="perfil"),

    url(r'^post$/?', post.post, name="post"),
]
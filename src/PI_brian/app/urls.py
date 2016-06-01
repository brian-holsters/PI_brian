# -*- coding: utf-8 -*-
from PI_brian.app.views.admin import emotes

__author__ = 'brian'

from django.conf.urls import url, include

from PI_brian.app.views import auth, index, post, perfil, api

urlpatterns= [
	url(r'^$/?', index.index, name="index"),

    url(r'^login$/?', auth.loginView, name="login"),
	url(r'^registro$/?', auth.registro, name="registro"),
	url(r'^logout$/?', auth.logout, name="logout"),

    url(r'^perfil/(?P<username>[\w\d]+)$/?', perfil.ver_perfil, name="perfil"),

    url(r'^post$/?', post.post, name="post"),
    url(r'^ajax_post/?', post.ajax_post),

    ## URLs de administración:
    url(r'^administracion/emotes/?$', emotes.lista, name="emotes"),
    url(r'^administracion/emotes/nuevo/?$', emotes.nuevo, name="nuevo_emote"),
    url(r'^administracion/emotes/(?P<emote_id>[\d]+)/editar/?$', emotes.editar, name="editar_emote"),

    #API:
    url(r'^buscador-usuarios/json$', api.buscar_usuario, name="buscar_usuarios")
]
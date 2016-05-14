# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from PI_brian.app.forms.auth import RegisterForm


def index(request):
    if request.user.is_anonymous():
        form = RegisterForm()
        return render_to_response("index/index_anonimo.html", {"form":form, "valor_aceptar":"Regístrame!", "ocultar_cancelar": True}, RequestContext(request))
    else:
        return render_to_response("index/index.html", {}, RequestContext(request))

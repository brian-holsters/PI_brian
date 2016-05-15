# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from PI_brian.app.forms.auth import RegisterForm


def index(request):
    if request.user.is_anonymous():
        form = RegisterForm()
        replacements = {"form":form, "valor_aceptar":"Regístrame!", "ocultar_cancelar": True}
        return render_to_response("index/index_anonimo.html", replacements, RequestContext(request))
    else:
        user = request.user
        return HttpResponseRedirect(reverse("perfil", kwargs={"username" : user.username}))

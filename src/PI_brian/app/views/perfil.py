# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from PI_brian.app.forms.post import PostForm


def ver_perfil(request, username):
    propietario = get_object_or_404(User, username=username)
    usuario = request.user

    # Diferenciar el perfil de uno mismo al de otro usuario:
    if usuario == propietario:
        return ver_propio_perfil(request)
    return ver_otro_perfil(request, propietario)


def ver_propio_perfil(request):
    usuario = request.user
    form = PostForm(usuario)
    posts = usuario.posts.filter().order_by("-fecha_creacion")
    replacements = {"posts": posts, "form": form, "valor_aceptar": "Publicar", "ocultar_cancelar": True}
    return render_to_response("perfil/propio.html", replacements, RequestContext(request))


def ver_otro_perfil(request, propietario):
    posts = propietario.posts.filter().order_by("-fecha_creacion")
    return render_to_response("perfil/otro.html", {"posts":posts, "propietario":propietario}, RequestContext(request))
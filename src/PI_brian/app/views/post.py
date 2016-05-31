# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import Http404, JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from PI_brian.app.forms.post import PostForm
from PI_brian.app.models import Post


def post(request):
    user = request.user
    if request.method == "POST":
        form = PostForm(user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            raise Exception("Formulario no válido")
    raise Http404()

def ajax_post(request):
    user = request.user
    if request.method == "POST":
        print request.POST
        respuesta_de = None
        if "respuesta_de" in request.POST:
            op = Post.objects.get(id=request.POST["respuesta_de"])
            respuesta_de = op

        form = PostForm(user, respuesta_de, request.POST)
        if form.is_valid():
            saved_post = form.save()
            if respuesta_de:
                return render_to_response("perfil/post.html", {"post":saved_post}, RequestContext(request))
            else:
                return render_to_response("perfil/post.html", {"post":saved_post}, RequestContext(request))
        print form.errors
        raise Exception("formulario no válido|{0}".format(form.errors))

    raise Exception("Petición no es por POST")

# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import Http404, JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from PI_brian.app.forms.post import PostForm


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
        form = PostForm(user, request.POST)
        if form.is_valid():
            saved_post = form.save()
            return render_to_response("index/post.html", {"post":saved_post}, RequestContext(request))
        else:
            raise Exception("formulario no valido")
    raise Exception("Petición no es por POST")

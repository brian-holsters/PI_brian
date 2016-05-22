# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import Http404, JsonResponse

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
            form.save()
            return JsonResponse({"ok":"Post publicado"})
        else:
            return JsonResponse({"Error":"Formulario no válido"})
    return JsonResponse({"Error":"La petición tiene que ser por POST"})

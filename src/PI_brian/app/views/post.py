# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import Http404

from PI_brian.app.forms.post import PostForm


def post(request):
    user = request.user
    print "-"*60
    print user
    print "-" * 60
    if request.method == "POST":
        form = PostForm(user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            raise Exception("Formulario no válido")
    raise Http404()
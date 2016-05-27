# -*- coding: utf-8 -*-
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from PI_brian.app.forms.emote import EmoteForm
from PI_brian.app.models import Emote

@staff_member_required(login_url="login")
def lista(request):
	emotes = Emote.objects.filter()
	return render_to_response("admin/emotes/lista.html", {"emotes":emotes}, RequestContext(request))


@staff_member_required(login_url="login")
def nuevo(request):
	if request.method == "POST":
		form = EmoteForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("emotes"))
	else:
		form = EmoteForm()
	return render_to_response("admin/emotes/nuevo.html", {"form":form}, RequestContext(request))
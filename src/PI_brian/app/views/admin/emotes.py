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
		if "cancelar" in request.POST:
			return HttpResponseRedirect(reverse("emotes"))
		form = EmoteForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("emotes"))
	else:
		form = EmoteForm()
	return render_to_response("admin/emotes/nuevo.html", {"form":form}, RequestContext(request))


@staff_member_required(login_url="login")
def editar(request, emote_id):
	emote = get_object_or_404(Emote, **{"id":emote_id})
	if request.method == "POST":
		if "cancelar" in request.POST:
			return HttpResponseRedirect(reverse("emotes"))
		form = EmoteForm(request.POST, request.FILES, instance=emote)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("emotes"))
	else:
		form = EmoteForm(instance=emote)

	return render_to_response("admin/emotes/editar.html", {"form":form, "emote": emote}, RequestContext(request))
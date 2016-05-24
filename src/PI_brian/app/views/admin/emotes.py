# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from PI_brian.app.models import Emote


def lista(request):
	emotes = Emote.objects.filter()
	return render_to_response("admin/emotes/lista.html", {"emotes":emotes}, RequestContext(request))

def nuevo(request):
	pass
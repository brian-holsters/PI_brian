# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response


# Create your views here.
from django.template import RequestContext


def index(request):
	if request.user.is_anonymous():
		return render_to_response("index_anonimo.html", {}, RequestContext(request))
	else:
		return render_to_response("index.html", {}, RequestContext(request))

def login(request):
	pass

def registro(request):
	pass
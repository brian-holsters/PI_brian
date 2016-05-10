# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	if request.user.is_anonymous():
		return render_to_response("index/index_anonimo.html", {}, RequestContext(request))
	else:
		return render_to_response("index/index.html", {}, RequestContext(request))

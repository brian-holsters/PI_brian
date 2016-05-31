# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from PI_brian.app.forms.post import RespuestaForm


def ajax_respuesta(request):
	if not request.method == "POST":
		raise Http404
	print request.POST
	user = request.user
	form = RespuestaForm(user, request.POST)
	if form.is_valid():
		respuesta = form.save()
		return render_to_response("perfil/respuesta.html", {"respuesta": respuesta}, RequestContext(request))
	print form.errors
	raise Exception("El formulario no es válido")
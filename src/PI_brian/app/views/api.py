# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import JsonResponse


def buscar_usuario(request):
	print "-"*60
	print request
	print "-"*60
	if "usuario" in request.GET:
		busqueda = request.GET["usuario"]
		usuarios = User.objects.filter(username__icontains=busqueda)
		json_usuarios = jsonify(usuarios)
		return JsonResponse(json_usuarios)
	raise Exception("PAAAM!")


def jsonify(usuarios):
	json_base = {"response": []}
	for usuario in usuarios:
		json_usuario = {
			"nombre" : usuario.username
		}
		json_base["response"].append(json_usuario)
	return json_base
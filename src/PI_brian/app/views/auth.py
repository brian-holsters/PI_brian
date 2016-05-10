# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def login(request):
	pass

def registro(request):
	pass

def reset_password(request):
	if(request.method == "POST"):
		if "username" in request.POST:
			user = User.objects.get(username__exact=request.POST["username"])
			password = User.objects.make_random_password()
			user.set_password(password)
			user.save()
			send_mail("Ha solicitado restablecer su contraseña", "su nueva contraseña es: {0}".format(password), settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
		return HttpResponseRedirect(reverse("index"))
	return render_to_response("forms/reset_password.html", {}, RequestContext(request))
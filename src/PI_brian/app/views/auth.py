# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from PI_brian.app.forms.auth import RegisterForm, LoginForm


def loginView(request):
	if request.method == "POST":
		if "cancelar" in request.POST:
			return HttpResponseRedirect(reverse("index"))
		else:
			form = LoginForm(request.POST)
			if form.is_valid():
				print form.cleaned_data
				user = authenticate(username=form.cleaned_data["usuario"], password=form.cleaned_data["password"])
				if user is not None and user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse("index"))
	else:
		form = LoginForm()
	return render_to_response("forms/auth/login.html", {"form" : form}, RequestContext(request))

def registro(request):
	if request.method == 'POST':
		if "cancelar" in request.POST:
			print "cancelar"
			return HttpResponseRedirect(reverse("index"))
		else:
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()

				# Una vez que hemos creado el usuario, iniciamos sesión con él
				print form.data
				return HttpResponseRedirect(reverse("login"))
	else:
		form = RegisterForm()

	return render_to_response('forms/auth/registro.html', {'form': form}, RequestContext(request))

def reset_password(request):
	if request.method == "POST":
		if "username" in request.POST:
			user = User.objects.get(username__exact=request.POST["username"])
			password = User.objects.make_random_password()
			user.set_password(password)
			user.save()
			send_mail("Ha solicitado restablecer su contraseña", "su nueva contraseña es: {0}".format(password), settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
		return HttpResponseRedirect(reverse("index"))
	return render_to_response("forms/reset_password.html", {}, RequestContext(request))
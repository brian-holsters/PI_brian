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
from django.contrib.auth import logout as user_logout

def loginView(request):
	if request.method == "POST":
		if "cancelar" in request.POST:
			return HttpResponseRedirect(reverse("index"))
		else:
			form = LoginForm(request.POST)
			if form.is_valid():
				user = authenticate(username=form.cleaned_data["usuario"], password=form.cleaned_data["password"])
				if user is not None and user.is_active:
					print "logando"
					login(request, user)
					return HttpResponseRedirect(reverse("index"))
	else:
		form = LoginForm()
	print "no logando"
	return render_to_response("auth/login.html", {"form" : form, "valor_aceptar":"Login"}, RequestContext(request))

def registro(request):
	if request.method == 'POST':
		if "cancelar" in request.POST:
			return HttpResponseRedirect(reverse("index"))
		else:
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()

				return HttpResponseRedirect(reverse("login"))
	else:
		form = RegisterForm()

	return render_to_response('auth/registro.html', {'form': form, "valor_aceptar":"Regístrame!"}, RequestContext(request))

def logout(request):
	user_logout(request)
	return HttpResponseRedirect(reverse("index"))

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
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from django import forms


class LoginForm(forms.Form):
	usuario = forms.CharField(label=u"Usuario", required=True)
	password = forms.CharField(label=u"Contraseña", required=True)

	## Comprobaciones del nombre de usuario:
	## Que sea un nombre de usuario válido
	def clean_username(self):
		username = self.cleaned_data['username']
		# El nombre de usuario ha de ser correcto
		if not re.match(r"[\w\d]+", username):
			raise forms.ValidationError(u"El nombre de usuario {0} no es válido. Sólo se aceptan nombres de usuarios que contengan caracteres alfanuméricos.".format(username))
		# Ha de existir un usuario activo con ese nombre de usuario
		if not User.objects.filter(username=username, is_active=True).exists():
			raise ValidationError(u"No existe ningún usuario con ese nombre.")
		# Si el nombre de usuario es válido y existe un usuario, devuelve el nombre de usuario
		return username

class RegisterForm(forms.Form):
	pass
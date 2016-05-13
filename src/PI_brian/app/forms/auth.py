# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction
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


class RegisterForm(forms.ModelForm):
	password2 = forms.CharField(label=u"confirme contraseña", widget = forms.PasswordInput(), required=True)
	class Meta:
		model = User
		fields = ["username", "email", "password", "password2"]

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields["username"] = forms.CharField(label=u"Nombre de usuario", max_length=64, required=True)
		self.fields["password"] = forms.CharField(label=u"contraseña", widget = forms.PasswordInput(), required=True)
		self.fields["password2"] = forms.CharField(label=u"confirme contraseña", widget = forms.PasswordInput(), required=True)
		self.fields["email"] = forms.EmailField(label=u"Correo electrónico", help_text = u"Dirección de correo electrónico para recuperar la contraseña", required=True)

		self.fields["first_name"] = forms.CharField(label=u"Nombre", max_length=64, required=True)
		self.fields["last_name"] = forms.CharField(label=u"Apellidos", max_length=64, required=True)

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		if cleaned_data.get("password") != cleaned_data.get("password2"):
			raise forms.ValidationError(u"Las contraseñas introducidas no coinciden")
		return cleaned_data

	@transaction.atomic
	def save(self, commit=True):
		# super(RegisterForm, self).save(commit=commit)
		user = User(username=self.cleaned_data["username"], email=self.cleaned_data["email"],first_name=self.cleaned_data["first_name"], last_name=self.cleaned_data["last_name"])
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user


class ChangePasswordForm(forms.Form):
	def __init__(self, user=None, *args, **kwargs):
		self.user = user
		super(ChangePasswordForm, self).__init__(*args, **kwargs)
		self.fields["old_password"] = forms.CharField(label=_(u"Contraseña actual"), widget = forms.PasswordInput(), required=True)
		self.fields["password1"] = forms.CharField(label=_(u"Contraseña nueva"), widget = forms.PasswordInput(), required=True)
		self.fields["password2"] = forms.CharField(label=_(u"Confirme contraseña"), widget = forms.PasswordInput(), required=True)

	def clean_old_password(self):
		old_password = self.cleaned_data['old_password']
		if not self.user.check_password(old_password):
			raise ValidationError("Contraseña incorrecta")
		return old_password

	def clean(self):
		cleaned_data = super(ChangePasswordForm, self).clean()
		if cleaned_data["password1"] != cleaned_data["password2"]:
			raise ValidationError("Las contraseñas no coinciden")
		return cleaned_data

	@transaction.atomic
	def save(self):
		user = self.user
		user.set_password(self.cleaned_data["password1"])
		user.save()
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import Model, DateTimeField, BooleanField, ImageField, ForeignKey
from django.contrib.auth.models import User

class Dibujo(Model):
	fecha_creacion = DateTimeField(verbose_name=u"fecha en la que se ha creado el objeto", auto_now=True)
	is_erased = BooleanField(null=False, default=False, verbose_name=u"Marca si se ha eliminado de forma lógica el objeto")
	dibujo = ImageField(verbose_name=u"dibujo asociado al objeto", null=False)

	user = ForeignKey(User, verbose_name=u"Usuario que ha publicado el dibujo", related_name="dibujos")
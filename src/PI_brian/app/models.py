# -*- coding: utf-8 -*-

from django.db.models import Model, DateTimeField, BooleanField, CharField, ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(Model):
    class Meta:
        ordering = ["fecha_creacion"]
    fecha_creacion = DateTimeField(verbose_name=u"fecha en la que se ha creado el objeto", auto_now=True)
    is_erased = BooleanField(null=False, default=False, verbose_name=u"Marca si se ha eliminado de forma lógica el objeto")
    texto = CharField(verbose_name=u"contenido del post", max_length=250, null=False)

    user = ForeignKey(User, verbose_name=u"Usuario que ha publicado el post", related_name="posts")

    @property
    def tiempo_desde_creacion(self):
        tiempo = timezone.now() - self.fecha_creacion
        result = Post._parse_tiempo(tiempo)
        return result

    @staticmethod
    def _parse_tiempo(tiempo):
        segundos = tiempo.seconds
        if segundos > 60*60*24:
            return str(segundos/(60*60*24)) + " dias"
        if segundos > 60*60:
            return str(segundos/(60*60)) + " horas"
        if segundos > 60:
            return str(segundos/60) + " minutos"
        return "un momento"
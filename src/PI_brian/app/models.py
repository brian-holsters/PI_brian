# -*- coding: utf-8 -*-

from django.db.models import Model, DateTimeField, BooleanField, CharField, ForeignKey, ImageField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(Model):
    class Meta:
        ordering = ["fecha_creacion"]

    fecha_creacion = DateTimeField(verbose_name=u"fecha en la que se ha creado el objeto", auto_now=True)
    is_erased = BooleanField(null=False, default=False, verbose_name=u"Marca si se ha eliminado de forma lógica el objeto")
    texto = CharField(verbose_name=u"contenido del post", max_length=250, null=False)
    emote = ForeignKey("Emote", verbose_name=u"icono que acompaña al Post", null=True, default=None)

    user = ForeignKey(User, verbose_name=u"Usuario que ha publicado el post", related_name="posts")

    def __unicode__(self):
        return self.texto[:20] + "... Escrito por " + self.user.username

    @property
    def tiempo_desde_creacion(self):
        tiempo = timezone.now() - self.fecha_creacion
        print tiempo
        result = Post._parse_tiempo(tiempo)
        return result

    @staticmethod
    def _parse_tiempo(tiempo):
        dias = tiempo.days
        horas = tiempo.seconds/(60*60)
        minutos = tiempo.seconds/60
        if dias > 0:
            return str(dias) + " dias"
        elif horas > 0:
            return str(horas) + " horas"
        elif minutos > 0:
            return str(minutos) + " minutos"
        else:
            return "un momento"

class Reply(Post):
    post = ForeignKey(Post, verbose_name=u"Post al que responde este", related_name="replies")

class Emote(Model):
    class Meta:
        ordering = ["nombre"]
    nombre = CharField(verbose_name=u"Nombre del emoticono", max_length=20)
    imagen = ImageField(verbose_name=u"Imagen del emoticono", upload_to="emotes")

    def __unicode__(self):
        return self.nombre
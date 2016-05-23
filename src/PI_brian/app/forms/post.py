# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils import timezone

from PI_brian.app.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["is_erased", "user"]
        texto = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        user = User.objects.get(username=user.username)
        self.user = user
        self.fecha_creacion = timezone.now()
        # self.fields["texto"].widget =

    def save(self):
        post = super(PostForm, self).save(commit=False)
        post.user = self.user
        post.fecha_creacion = self.fecha_creacion
        post.is_erased = False
        post.texto = self.cleaned_data["texto"]
        post.save()
        return post
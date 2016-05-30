# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.utils import timezone

from PI_brian.app.models import Post, Emote


class PostForm(ModelForm):
    emote_id = forms.CharField()

    class Meta:
        model = Post
        exclude = ["is_erased", "user", "emote"]
        texto = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        user = User.objects.get(username=user.username)
        self.user = user
        self.fecha_creacion = timezone.now()
        self.emote = None

    def save(self, commit=False):
        post = super(PostForm, self).save(commit=commit)
        post.user = self.user
        post.fecha_creacion = self.fecha_creacion
        post.is_erased = False
        post.texto = self.cleaned_data["texto"]
        post.emote = self.cleaned_data["emote"]
        post.save()
        return post

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        if "emote_id" in cleaned_data:
            cleaned_data["emote"] = Emote.objects.get(id=cleaned_data["emote_id"])
        return cleaned_data
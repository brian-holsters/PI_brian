# -*- coding: utf-8 -*-
from django.contrib import admin
from PI_brian.app.models import Post, Reply, Emote

admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Emote)


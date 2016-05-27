# -*- coding: utf-8 -*-
from django.forms import ModelForm
from PI_brian.app.models import Emote


class EmoteForm(ModelForm):
	class Meta:
		model = Emote
		exclude = []
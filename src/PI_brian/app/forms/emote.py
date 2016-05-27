# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from stickyuploads.widgets import StickyUploadWidget
from PI_brian.app.models import Emote


class EmoteForm(ModelForm):
	class Meta:
		model = Emote
		exclude = []

	def __init__(self, *args, **kwargs):
		super(EmoteForm, self).__init__(*args, **kwargs)
		self.fields["imagen"].widget = StickyUploadWidget()

	def clean_imagen(self):
		if "imagen" in self.cleaned_data:
			return self.cleaned_data["imagen"]
		if "id" in self.instance:
			return self.instance.imagen
		raise ValidationError("Este campo es obligatorio")

class EditEmoteForm(ModelForm):
	class Meta:
		model = Emote
		exclude = []


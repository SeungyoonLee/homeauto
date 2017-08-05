# -*- coding: utf-8 -*-
from django import forms
from .models import LightControl

class LightControlForm(forms.ModelForm):
    class Meta:
        model = LightControl
        fields = ('location', 'switch_on',)

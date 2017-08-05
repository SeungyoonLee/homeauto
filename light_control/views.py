# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def light_list(request):
    return render(request, 'light_control/light_list.html', {})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import LightControl

# Create your views here.
def light_list(request):
    lights = LightControl.objects.all()
    return render(request, 'light_control/light_list.html', {'lights': lights})

def switch(request):
    print(request.GET['location'])
    print(request.GET['switch_on'])
    light = LightControl.objects.get(location=request.GET['location'])
    if eval(request.GET['switch_on']):
        light.on()
    else:
        light.off()
    return redirect('light_list')

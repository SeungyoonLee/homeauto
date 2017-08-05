# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class LightControl(models.Model):
    location = models.CharField(max_length=100)
    switch_on = models.BooleanField()
    last_date = models.DateTimeField(default=timezone.now)

    def on(self):
        self.last_date = timezone.now()
        self.switch_on = True
        self.save()

    def off(self):
        self.last_date = timezone.now()
        self.switch_on = False

        self.save()

    def __str__(self):
        return self.location

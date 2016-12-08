# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ExampleSimple(models.Model):
    direccion = models.CharField(max_length=50, default="")
    float_1 = models.FloatField(default=0.0)
    float_2 = models.FloatField(default=0.0)
    float_3 = models.FloatField(default=0.0)
    float_4 = models.FloatField(default=0.0)
    float_5 = models.FloatField(default=0.0)
    float_6 = models.FloatField(default=0.0)
    float_7 = models.FloatField(default=0.0)
    float_8 = models.FloatField(default=0.0)
    float_9 = models.FloatField(default=0.0)
    def __unicode__(self):
        return u'%s' % (self.direccion) 
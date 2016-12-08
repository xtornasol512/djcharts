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

    def _suma_campos(self):
        "Returns suma de campos"

        return '%f' % (self.float_1 + self.float_2 + self.float_3 + self.float_4+ self.float_5+ self.float_6+ self.float_7)
    suma = property(_suma_campos)

    def __unicode__(self):
        return u'%s' % (self.direccion) 
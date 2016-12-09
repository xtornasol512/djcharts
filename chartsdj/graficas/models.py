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


class NotasPeriodico(models.Model):
    """ Modelo de notas de periodico reportadas por estado en Mexico """
    estado = models.CharField(max_length=10, default="")
    r_2006 = models.FloatField(default=0.0)
    r_2007 = models.FloatField(default=0.0)
    r_2008 = models.FloatField(default=0.0)
    r_2009 = models.FloatField(default=0.0)
    r_2010 = models.FloatField(default=0.0)
    r_2011 = models.FloatField(default=0.0)
    r_2012 = models.FloatField(default=0.0)
    r_2013 = models.FloatField(default=0.0)
    r_2014 = models.FloatField(default=0.0)
    r_2015 = models.FloatField(default=0.0)
    r_2016 = models.FloatField(default=0.0)

    def _suma_campos(self):
        "Returna suma de campos"
        return float(self.r_2006 + self.r_2007 + self.r_2008
                    + self.r_2009 + self.r_2010 + self.r_2011 + self.r_2012
                    + self.r_2013 + self.r_2014 + self.r_2015 + self.r_2016)
    suma = property(_suma_campos)

    def __unicode__(self):
        return u'%s' % (self.estado)

class NotasPorEstado(models.Model):
    """ Notas por Estado """
    estado = models.CharField(max_length=10, default="")
    year = models.CharField(max_length=10, default="", verbose_name='Año')
    sucesos = models.IntegerField(default=0)

    def __unicode__(self):
        #Regresa el nombre del objeto , en este caso estado
        return u'%s' % (self.estado)

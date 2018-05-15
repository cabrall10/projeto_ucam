# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Estoque(models.Model):
    material = models.OneToOneField('Material',on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=8, decimal_places=3)

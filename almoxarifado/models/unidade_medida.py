# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    abreviacao = models.CharField(max_length=3, unique=True, verbose_name='Abreviação')

    class Meta:
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return "{} ({})".format(self.nome, self.abreviacao)

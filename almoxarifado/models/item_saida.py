# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ItemSaida(models.Model):
    saida = models.ForeignKey('Saida', related_name="item_saida", on_delete=models.PROTECT)
    material = models.ForeignKey('Material', on_delete=models.PROTECT)
    quantidade = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Saída de material'

    def __str__(self):
        return "{}".format(self.material.nome)

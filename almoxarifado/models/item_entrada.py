# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ItemEntrada(models.Model):
    """Será o material pertencente a entrada de um nova compra. O funcionário
       do almoxarifado sempre informar o material, a quantidade e o valor de
       aquisicao.
    """
    entrada = models.ForeignKey('Entrada', related_name="itemEntrada_material", on_delete=models.PROTECT)
    material = models.ForeignKey('Material', related_name="itemEntrada_material", on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.material.nome, self.entrada.nota_fiscal)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    @receiver(post_save, sender='almoxarifado.ItemEntrada')
    def adicionar_ao_estoque(sender, instance, **kwargs):
        Estoque = apps.get_model('almoxarifado', 'Estoque')
        try:
            estoque = Estoque.objects.get(material=instance.material)
            estoque.quantidade += instance.quantidade
            estoque.save()
        except Estoque.DoesNotExist:
            estoque = Estoque.objects.create(material=instance.material, quantidade=instance.quantidade)

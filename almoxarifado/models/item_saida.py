# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .estoque import Estoque


class ItemSaida(models.Model):
    saida = models.ForeignKey('Saida', related_name="item_saida", on_delete=models.PROTECT)
    material = models.ForeignKey('Material', on_delete=models.PROTECT)
    quantidade = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Saída de material'

    def __str__(self):
        return "{}".format(self.material.nome)

    def clean(self):
        estoque = Estoque.objects.get(material=self.material)
        if self.quantidade > estoque.quantidade:
            raise ValidationError('Não há estoque suficiente (Estoque: {}).'.format(estoque.quantidade))

    @receiver(post_save, sender='almoxarifado.ItemSaida')
    def adicionar_ao_estoque(sender, instance, **kwargs):
        Estoque = apps.get_model('almoxarifado', 'Estoque')
        estoque = Estoque.objects.get(material=instance.material)
        estoque.quantidade -= instance.quantidade
        estoque.save()

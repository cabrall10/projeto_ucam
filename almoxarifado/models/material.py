# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Material(models.Model):
    CATEGORIA_CHOICES = (
        ('estocavel', 'Estocável'),
        ('n_estocavel', 'Não estocável'),
        ('cons_geral', 'Consumo geral'),
        ('manutencao', 'Manutenção'),
    )

    nome = models.CharField(max_length=255)
    unidade_medida = models.ForeignKey('UnidadeMedida', on_delete=models.PROTECT)
    categoria = models.CharField(max_length=255, choices=CATEGORIA_CHOICES)

    class Meta:
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return self.nome

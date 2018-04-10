# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=255, verbose_name='Razão Social')
    segmento = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.EmailField()
    nome_atendente = models.CharField(max_length=255, verbose_name='Nome do atendente')

    class Meta:
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.razao_social

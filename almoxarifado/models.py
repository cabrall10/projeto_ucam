# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=255)
    segmento = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.EmailField()
    nome_atendente = models.CharField(max_length=255)

    def __str__(self):
        return self.razao_social

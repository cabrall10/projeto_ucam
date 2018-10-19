# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=255)
    "cpf = models.CharField(max_length=255)"
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Setor'

    def __str__(self):
        return self.nome

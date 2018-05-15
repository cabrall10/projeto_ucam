# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class PessoaFisica(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Pessoa Física'

    def __str__(self):
        return self.nome

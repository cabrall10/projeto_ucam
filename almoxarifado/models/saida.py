# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models


class Saida(models.Model):
    solicitante = models.ForeignKey('PessoaFisica', related_name='saida_solicitante', on_delete=models.PROTECT)
    data = models.DateField(auto_now=True)
    observacao = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Saída de material'

    def __str__(self):
        return '{} {}'.format(self.solicitante.nome, self.data)

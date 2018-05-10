# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models


class Saida(models.Model):
    solicitante = models.ForeignKey('PessoaFisica', on_delete=models.PROTECT)
    data = models.DateField(auto_now=True)
    observacao = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Histórico de saída'

    def __str__(self):
        return self.solicitante, self.data

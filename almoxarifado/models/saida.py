# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Saida(models.Model):
    solicitante = models.ForeignKey('PessoaFisica', on_delete=models.PROTECT)
    data = models.DateField(auto_now=True)
    observacao = models.TextField()

    def __str__(self):
        return self.solicitante, self.data

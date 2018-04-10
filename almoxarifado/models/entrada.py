# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Entrada(models.Model):
    """É o cadastro de uma nova compra realizada pela UCAM. O funcionario
       ira cadastrar a nota fiscal com data, fornecedor e ira informar os
       itens adquiridos
       ** pesquisar sobre InlineModelAdmin / StackedInline **
    """
    nota_fiscal = models.CharField(max_length=255)
    fornecedor = models.ForeignKey('Fornecedor', related_name="entradas_fornecedor", on_delete=models.PROTECT)
    data = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.nota_fiscal

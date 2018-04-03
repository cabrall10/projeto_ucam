# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    abreviacao = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return "{} ({})".format(self.nome, self.abreviacao)


class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=255)
    segmento = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.EmailField()
    nome_atendente = models.CharField(max_length=255)

    def __str__(self):
        return self.razao_social


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

    def __str__(self):
        return self.nome


class ItemEntrada(models.Model):
    """Será o material pertencente a entrada de um nova compra. O funcionário
       do almoxarifado sempre informar o material, a quantidade e o valor de
       aquisicao.
    """
    entrada = models.ForeignKey('Entrada', on_delete=models.PROTECT)
    material = models.ForeignKey('Material', on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.material.nome, self.entrada.nota_fiscal)


class Entrada(models.Model):
    """É o cadastro de uma nova compra realizada pela UCAM. O funcionario
       ira cadastrar a nota fiscal com data, fornecedor e ira informar os
       itens adquiridos
       ** pesquisar sobre InlineModelAdmin / StackedInline **
    """
    nota_fiscal = models.CharField(max_length=255)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.PROTECT)
    data = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.nota_fiscal

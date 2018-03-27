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


class Produto(models.Model):
    CATEGORIA_CHOICES = (
        ('estocavel', 'Estocável'),
        ('n_estocavel', 'Não estocável'),
        ('cons_geral', 'Consumo geral'),
        ('manutencao', 'Manutenção'),
    )

    nome = models.CharField(max_length=255)
    unidade_medida = models.CharField(max_length=255)
    custo = models.CharField(max_length=255)
    validade = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255, choices=CATEGORIA_CHOICES)
    observacao = models.TextField()

    def __str__(self):
        return self.nome_produto

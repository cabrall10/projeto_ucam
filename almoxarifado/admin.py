# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *



class ItemEntradaAdmin(admin.TabularInline):
    autocomplete_fields = ['material']
    model = ItemEntrada
    min_num = 1
    extra = 0

class ItemSaidaAdmin(admin.TabularInline):
    autocomplete_fields = ['material']
    model = ItemSaida
    min_num = 1
    extra = 0

class SaidaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['solicitante']
    inlines = (ItemSaidaAdmin,)
    list_filter = ('data',)

class EntradaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['fornecedor']
    inlines = (ItemEntradaAdmin,)
    search_fields = ['nota_fiscal', 'fornecedor__razao_social', 'itemEntrada_material__material__nome']
    list_filter = ('data',)

class FornecedorAdmin(admin.ModelAdmin):
    search_fields = ['razao_social', 'segmento']
    list_filter = ('segmento',)

class MaterialAdmin(admin.ModelAdmin):
    search_fields= ['nome', 'categoria']
    list_filter = ('categoria',)

class UnidadeMedidaAdmin(admin.ModelAdmin):
    search_fields= ['nome', 'abreviacao']
    list_filter = ('abreviacao',)

class PessoaFisicaAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'cpf']



admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(UnidadeMedida, UnidadeMedidaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Saida, SaidaAdmin)
admin.site.register(PessoaFisica, PessoaFisicaAdmin)
admin.site.register(Estoque)

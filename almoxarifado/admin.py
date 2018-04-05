# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Fornecedor, UnidadeMedida, Entrada, ItemEntrada, Material


class ItemEntradaAdmin(admin.TabularInline):
    model = ItemEntrada


class EntradaAdmin(admin.ModelAdmin):
    inlines = (ItemEntradaAdmin,)
    search_fields = ['nota_fiscal', 'fornecedor__razao_social']
    list_filter = ('data',)

class FornecedorAdmin(admin.ModelAdmin):
    search_fields = ['razao_social', 'segmento']
    list_filter = ('segmento',)

class MaterialAdmin(admin.ModelAdmin):
    search_fields= ['nome', 'categoria']
    list_filter = ('categoria',)

class Unidade_MedidaAdmin(admin.ModelAdmin):
    search_fields= ['nome', 'abreviacao']
    list_filter = ('abreviacao',)



admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(UnidadeMedida, Unidade_MedidaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material, MaterialAdmin)

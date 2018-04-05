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


admin.site.register(Fornecedor)
admin.site.register(UnidadeMedida)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material)

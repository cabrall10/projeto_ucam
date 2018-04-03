# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Fornecedor, UnidadeMedida, Entrada, ItemEntrada, Material

class ItensAdicionadosTabularInline(admin.TabularInline):
    model = ItemEntrada

class EntradaItens(admin.ModelAdmin):
    inlines = [ItensAdicionadosTabularInline]
    class Meta:
        model = Entrada

admin.site.register(Fornecedor)
admin.site.register(UnidadeMedida)
admin.site.register(Entrada, EntradaItens)
admin.site.register(ItemEntrada)
admin.site.register(Material)

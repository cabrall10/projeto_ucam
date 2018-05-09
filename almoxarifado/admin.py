# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models.fornecedor import Fornecedor
from .models.item_entrada import ItemEntrada
from .models.unidade_medida import UnidadeMedida
from .models.entrada import Entrada
from .models.material import Material
from .models.item_saida import ItemSaida
from .models.pessoa_fisica import PessoaFisica
from .models.saida import Saida



class ItemEntradaAdmin(admin.TabularInline):
    autocomplete_fields = ['material']
    model = ItemEntrada
    min_num = 1
    extra = 0

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



admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(UnidadeMedida, UnidadeMedidaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ItemSaida)
admin.site.register(Saida)
admin.site.register(PessoaFisica)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.contrib import admin

from .models import *


from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from weasyprint import HTML
from django_object_actions import DjangoObjectActions


class ItemEntradaAdmin(admin.TabularInline):
    autocomplete_fields = ['material']
    model = ItemEntrada
    min_num = 1
    extra = 0
    ordering = ["material__nome"]

class ItemSaidaAdmin(admin.TabularInline):
    autocomplete_fields = ['material']
    model = ItemSaida
    min_num = 1
    extra = 0

class SaidaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['solicitante']
    inlines = (ItemSaidaAdmin,)
    list_filter = ('data',)
    actions = ['relatorio_de_saidas',]

    def relatorio_de_saidas(self, request, queryset):
        html_string = render_to_string('reports/relatorio_saidas.html', {'objects': queryset})
        obj = datetime.now().timestamp()

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
        return response
    relatorio_de_saidas.short_description = "Gerar relatório de saidas"

class EntradaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['fornecedor']
    inlines = (ItemEntradaAdmin,)
    search_fields = ['nota_fiscal', 'fornecedor__razao_social', 'itemEntrada_material__material__nome']
    list_filter = ('data',)
    actions = ['relatorio_de_entradas',]

    def relatorio_de_entradas(self, request, queryset):
        html_string = render_to_string('reports/relatorio_entradas.html', {'objects': queryset})
        obj = datetime.now().timestamp()

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
        return response
    relatorio_de_entradas.short_description = "Gerar relatório de entradas"

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    search_fields = ['razao_social', 'segmento']
    list_filter = ('segmento',)

class MaterialAdmin(admin.ModelAdmin):
    search_fields= ['nome', 'categoria']
    list_filter = ('categoria',)

class UnidadeMedidaAdmin(admin.ModelAdmin):
    search_fields= ['nome', 'abreviacao']
    list_filter = ('abreviacao',)

class SetorAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'cpf']

#Mostra o campo quantidade do Modelo Estoque no site Admin
class EstoqueAdmin(admin.ModelAdmin):
    search_fields = ['material']
    list_display = ('material','quantidade')

# ativando este comando: @admin.register(ItemEntrada), registra na pagina inicial o modelo
#Item Entrada
class ReportAdmin(DjangoObjectActions, admin.ModelAdmin):
    search_fields = ['entrada, material']
    list_display = ('material','quantidade')

    def generate_pdf(self, request, obj):
        html_string = render_to_string('reports/pdf_template.html', {'obj': obj})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj));

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj)
            return response

        return response

    generate_pdf.label = 'Gerar PDF'
    generate_pdf.short_description = 'Clique para gerar o PDF dessa ordem de serviço'

    change_actions = ('generate_pdf',)


admin.site.register(UnidadeMedida, UnidadeMedidaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Saida, SaidaAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(Estoque, EstoqueAdmin)

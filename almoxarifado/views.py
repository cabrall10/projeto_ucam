# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def relatorio_entrada(request):
    return render(request, 'relatorio_entrada.html')

def relatorio_saida(request):
    return render(request, 'relatorio_saida.html')

def entradas(request):
    return render(request, 'entradas.html')

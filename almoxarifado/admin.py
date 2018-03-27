# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Produto, Fornecedor, UnidadeMedida


admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(UnidadeMedida)

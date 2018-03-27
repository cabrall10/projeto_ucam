# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Fornecedor, UnidadeMedida


admin.site.register(Fornecedor)
admin.site.register(UnidadeMedida)

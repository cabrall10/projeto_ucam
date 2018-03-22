# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Fornecedor

from .models import Produto

admin.site.register(Fornecedor)

admin.site.register(Produto)

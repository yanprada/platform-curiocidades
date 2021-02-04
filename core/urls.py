# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

import core.dash_piracicaba.dash_receitas
import core.dash_piracicaba.dash_receitas_pct
import core.dash_piracicaba.dash_despesas
import core.dash_piracicaba.dash_despesas_pct
import core.dash_piracicaba.dash_despesas_fun
import core.dash_piracicaba.dash_vereadores
import core.dash_piracicaba.dash_pref_luci
import core.dash_piracicaba.dash_pref_1
import core.dash_piracicaba.dash_pref_2
urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files]
    
]

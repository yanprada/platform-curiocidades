# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include, re_path

from app import views
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

    # The home page
    path('', views.index, name='home'),

    # pira resumo
    path('pira_resumo', views.piraresumo, name='pira_resumo'),

    # pira pref receitas
    path('pira_pref_rec', views.piraprefrec, name='pira_pref_rec'),

    # pira pref despesas
    path('pira_pref_des', views.piraprefdes, name='pira_pref_des'),

    # cam sessoes
    path('pira_cam_sessoes', views.piracamsessoes, name='pira_cam_sessoes'),

    # covid-casos
    path('pira_covid_casos', views.piracovidcasos, name='pira_covid_casos'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]

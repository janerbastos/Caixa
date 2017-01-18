# -*- encoding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'financeiro'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plano_contas/$', views.manage_plano_conta, name='plano_conta'),
    url(r'^plano_contas/(?P<action>\w+)/$', views.manage_plano_conta, name='plano_conta'),
    url(r'^plano_contas/(?P<action>\w+)/(?P<plano_conta_id>\d+)/$', views.manage_plano_conta, name='plano_conta'),
]

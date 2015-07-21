# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'accounting_tools.views',

    url(r'^subvention/(?P<ypk>[0-9]+)/export$', 'export_demands_yearly'),
    url(r'^subvention/export_all$', 'export_all_demands'),

    url(r'^invoice/(?P<pk>[0-9]+)/pdf/', 'invoice_pdf'),
    url(r'^invoice/(?P<pk>[0-9]+)/bvr/', 'invoice_bvr'),

    url(r'^withdrawal/(?P<pk>[0-9]+)/pdf/', 'withdrawal_pdf'),
    url(r'^internaltransfer/(?P<pk>[0-9]+)/pdf/', 'internaltransfer_pdf'),
    url(r'^expenseclaim/(?P<pk>[0-9]+)/pdf/', 'expenseclaim_pdf'),
)

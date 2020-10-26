#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.OauthLoginView.as_view(), name="oauth_index"),
    url(r'^callback/(?P<name>[a-z][a-z0-9]+)$',
        views.OauthCallbackView.as_view(), name="oauth_callback"),

    url(r'^confirm$', views.confirm, name="oauth_confirm"),

    url(r'^sessiontoken$', views.sessiontoken, name="oauth_sessiontoken"),
    url(r'^error$', views.error, name="oauth_error"),
]

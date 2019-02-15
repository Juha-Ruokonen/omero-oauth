#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    'django.views.generic.simple',

    url(r'^$', views.OauthLoginView.as_view(), name="oauth_index"),
    url(r'^callback$', views.OauthCallbackView.as_view(),
        name="oauth_callback"),
)

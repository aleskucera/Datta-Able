# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

from .views import device_list, device_create, device_page

app_name = 'devices'

urlpatterns = [
    path('list/', device_list, name='device-list'),
    path('add/', device_create, name='device-create'),
    path('device/<int:device_id>/', device_page, name='device-page'),
]

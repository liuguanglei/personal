# coding: utf-8

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^get_qr_pic/$', views.get_qr_pic, name='get_qr_pic')
]

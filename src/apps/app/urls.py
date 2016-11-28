# coding: utf-8

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^get_bk_pic/$', views.get_bk_pic, name='get_bk_pic')
]

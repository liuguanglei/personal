# coding: utf-8

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^get_newest_term/$', views.get_newest_term, name='get_newest_term')
]

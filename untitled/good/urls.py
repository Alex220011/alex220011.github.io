from django.contrib import admin
from django.urls import path, re_path
from good import views

urlpatterns = [
    path('', views.home, name="home"),
    re_path(r'^(?P<id>\d+)/$', views.start_visit, name='start_visit'),
]

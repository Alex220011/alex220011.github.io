from django.conf.urls import path, url, include
from . import views

urlpatterns = [
    url(r'', views.popi),
    path(r'relese/', views.rilize, name='rilize'),
]
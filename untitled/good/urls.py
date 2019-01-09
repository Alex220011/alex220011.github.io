from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from good import views


urlpatterns = [
   # path('admin/', admin.site.urls),
   # path('', views.home, name="home"),
    url(r'^(?P<id>\d+)/$', views.start_visit, name='start_visit'),
    path('', views.home, name="home"),
]

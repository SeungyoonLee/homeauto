from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.light_list, name='light_list'),
]

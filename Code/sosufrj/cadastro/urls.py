from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.campos, name='campos'),
    url(r'^protocolo/$', views.protocolo, name='protocolo'),
]

#URLs aqui

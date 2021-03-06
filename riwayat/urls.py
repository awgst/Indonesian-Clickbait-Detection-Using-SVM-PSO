from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^adm-result/$', views.getPredict),
    url(r'^hapusdata/', views.hapusData),
]

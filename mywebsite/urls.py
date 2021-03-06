from django.conf.urls import url, include
from django.contrib import admin

from . import views
from riwayat.views import getPredict as riwayatpredict
from riwayat.views import hapusData as hapusdata

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^disclaimer/', include('disclaimer.urls')), 
    url(r'^about/', include('about.urls')),
    url(r'^dashboard/', include('dashboard.urls'), name="dashboard"),
    url(r'^riwayat/', include('riwayat.urls')),
    url(r'^adm-result/$', riwayatpredict),
    url(r'^hapusdata/', hapusdata),
    url(r'^dataset/', include('training.urls')),
    url(r'^pengujian/', include('pengujian.urls')),
    url(r'^modelSVM/', include('modelSVM.urls')),
    url(r'^$', views.index, name='home'),
    url(r'^login/', views.loginView, name='login'),
    url(r'^logout/', views.logoutView, name='logout'),
    url(r'^result/$', views.getPredict)
]

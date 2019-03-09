from django.conf.urls import url, include
from django.contrib import admin
from app2 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'app/', include('app.urls')),
    url(r'app2', include('app2.urls')),
    url(r'year/(?P<year>[0-9]{4})/', views.year, name="when"),
    url(r'year2', views.year2),
]

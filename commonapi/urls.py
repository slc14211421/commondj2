from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'seturl', views.seturl),
    url(r'geturl', views.geturl),
]
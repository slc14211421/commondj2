from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [

    url(r'tag/(?P<pk>[0-9]+)$', views.TagView.as_view(), name='tag'),
    url(r'post2/(?P<pk>[0-9]+)$', views.PostDetailView.as_view(), name='detail'),
    url(r'archives2/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'category2/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'index2$', views.IndexView.as_view(), name='index'),

    url(r'category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'post/(?P<pk>[0-9]+)$', views.detail, name='detail'),
    url(r'index$', views.index, name='index'),
]
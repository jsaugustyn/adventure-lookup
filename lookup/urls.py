from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AdventureView.as_view(), name='index'),
    url(r'^adventures/(?P<pk>[0-9]+)/$', views.AdventureDetailView.as_view(), name='adventure-detail'),
    url(r'^adventures/new/$', views.AddAdventure.as_view(), name='add-adventure'),
    url(r'^adventures/(?P<pk>\d+)/update/$', views.AdventureUpdate.as_view(), name='adventure-update'),
    url(r'^adventures/(?P<pk>\d+)/delete/$', views.AdventureDelete.as_view(), name='adventure-delete')
]
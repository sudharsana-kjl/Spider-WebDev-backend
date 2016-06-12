from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$',views.searchStud,name = 'viewStud'),

    url(r'^(?P<id>\d+)/edit/$',views.editStud,name='editStud'),
]
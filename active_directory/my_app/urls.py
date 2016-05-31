from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_user/', views.add_user, name='add_user'),
    url(r'^remove_user/', views.remove_user, name='remove_user'),
    url(r'^list_users/', views.list_users, name='list_users'),
    url(r'^run_delete/(?P<user_del>\w+)/$', views.run_delete, name='run_delete'),

]

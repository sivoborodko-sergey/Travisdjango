from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registration/$', views.registration, name='registr'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
]

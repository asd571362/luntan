from django.conf.urls import url
from apps import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^register/$', views.register),
    url(r'^register/register_post/$', views.register_post),
    url(r'^register/uname_re_vf/$', views.uname_re_vf),
    url(r'^register/login_post/$', views.login_post),
]

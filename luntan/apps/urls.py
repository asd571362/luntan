from django.conf.urls import url
from apps import views

urlpatterns = [
    url(r'^register/$', views.register),
]

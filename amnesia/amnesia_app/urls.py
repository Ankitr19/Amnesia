from django.conf.urls import patterns, url
from . import views

app_name = 'amnesia_app'

urlpatterns = [
    url(r'^home$', views.home, name="home"),
    #url(r'^home$', views.home, name="home"),

]
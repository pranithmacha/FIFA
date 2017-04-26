from django.conf.urls import url
from league import views

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^create', views.create, name='create'),
]

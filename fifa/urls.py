from django.conf.urls import url
from fifa import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]

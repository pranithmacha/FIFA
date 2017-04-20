from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from league import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^login_successful$', views.login_success, name='login_success'),
    url(r'', include('league.urls')),
]

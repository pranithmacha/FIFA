from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from league import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^login_successful$', views.login_success, name='login_success'),
    url(r'', include('league.urls')),
]

if not settings.DEBUG:
    urlpatterns.append(url(r'^static/(?P<path>.*)$', serve,
                       {'document_root': settings.STATIC_ROOT}))

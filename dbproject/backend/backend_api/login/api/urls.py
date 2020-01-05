from django.urls import path, re_path
from .views import login_view, register_view, login_admin_view, register_admin_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^login/$', csrf_exempt(login_view), name='normal-login'),
    re_path(r'^register/$', csrf_exempt(register_view), name='normal-register'),
    re_path(r'^admin/login/$', csrf_exempt(login_admin_view), name='admin-login'),
    re_path(r'^admin/register/$', csrf_exempt(register_admin_view), name='admin-register')
]

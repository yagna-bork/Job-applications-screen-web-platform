from django.urls import path, re_path
from .views import get_all_jobs_view, get_all_available_jobs_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^all_jobs/$', get_all_jobs_view, name='get-all-jobs'),
    re_path(r'^all_available_jobs/$', get_all_available_jobs_view, name='get-all-available-jobs'),
    re_path(r'^all_not_available_jobs/$', get_all_available_jobs_view, name='get-all-not-available-jobs'),
]

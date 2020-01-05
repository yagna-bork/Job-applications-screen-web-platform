from django.urls import path, re_path, include
from .views import submit_new_application_view, db_submit_feedback_view, get_feedback_to_review_view, get_db_application_feedback_user_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^submit/$', csrf_exempt(submit_new_application_view), name='submit-application'),
    re_path(r'^submit_feedback/$', csrf_exempt(db_submit_feedback_view), name='submit-db-feedback'),
    path('accepted_applications/', csrf_exempt(get_feedback_to_review_view), name='get-accepted-applications'),
    path('feedback/', csrf_exempt(get_db_application_feedback_user_view), name='get-feedback-for-user'),
]

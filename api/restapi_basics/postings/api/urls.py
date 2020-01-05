from .views import BlogPostRudView, BlogPostAPIView
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^(?P<pk>\d+)$', BlogPostRudView.as_view(), name='post-rud'),
    re_path(r'^$', BlogPostAPIView.as_view(), name='post-list'), #get list, post new posting
]

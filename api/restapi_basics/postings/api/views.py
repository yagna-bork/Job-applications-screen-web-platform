from .. models import BlogPost
from rest_framework import generics, mixins, permissions
from . serializers import BlogPostSerializer
from django.db.models import Q
from .permissions import IsOwnerOrReadOnly


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
  lookup_field = 'pk'
  serializer_class = BlogPostSerializer
  permission_classes = [IsOwnerOrReadOnly]
  
  #kind of an endpoint
  def get_queryset(self):
    return BlogPost.objects.all()

  def get_serializer_context(self, *args, **kwargs):
    return {'request': self.request}

class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  # lookup_field = 'pk'
  serializer_class = BlogPostSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  #kind of an endpoint
  def get_queryset(self):
    qs = BlogPost.objects.all()
    query = self.request.GET.get('q') #somehow q in http get request will contain query??
    print(query)A
    if query is not None:
      qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct() #query passes when
    return qs                                                        #blog has keywords in title or content
  
  #allows for customizing serializer for mixins to do most of work
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def get_serializer_context(self, *args, **kwargs):
    return {'request': self.request}
